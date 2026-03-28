"""Handlers for tariffs display and multi-step tariff quiz.

The quiz collects 2–3 answers via FSM, then shows a personalized
tariff recommendation with a short "thinking" delay.
"""

import asyncio

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline import (
    tariff_actions_kb,
    quiz_start_kb,
    quiz_crm_kb,
    quiz_goal_kb,
    quiz_lose_clients_kb,
    quiz_manual_kb,
    quiz_result_kb,
)
from texts.messages import (
    TARIFFS,
    QUIZ_INTRO,
    QUIZ_Q1_CRM,
    QUIZ_Q2_GOAL,
    QUIZ_Q3_LOSE_CLIENTS,
    QUIZ_Q3_MANUAL,
    QUIZ_THINKING,
    build_quiz_result,
)

router = Router()


# --- Tariff Quiz FSM ---

class TariffQuiz(StatesGroup):
    """FSM states for the multi-step tariff picker."""
    q1_crm = State()
    q2_goal = State()
    q3_detail = State()


# --- Tariffs display (unchanged) ---

@router.callback_query(F.data == "tariffs")
async def show_tariffs(callback: CallbackQuery, state: FSMContext) -> None:
    """Display all 3 tariff plans."""
    await state.clear()
    await callback.answer()
    await callback.message.edit_text(TARIFFS, reply_markup=tariff_actions_kb())


# --- Quiz entry ---

@router.callback_query(F.data == "pick_tariff")
async def pick_tariff_intro(callback: CallbackQuery, state: FSMContext) -> None:
    """Show quiz intro with 'Start' button."""
    await state.clear()
    await callback.answer()
    await callback.message.edit_text(QUIZ_INTRO, reply_markup=quiz_start_kb())


@router.callback_query(F.data == "quiz_start")
async def quiz_ask_crm(callback: CallbackQuery, state: FSMContext) -> None:
    """Q1 — ask if user has a booking system."""
    await state.set_state(TariffQuiz.q1_crm)
    await callback.answer()
    await callback.message.edit_text(QUIZ_Q1_CRM, reply_markup=quiz_crm_kb())


# --- Q1: CRM answer ---

@router.callback_query(TariffQuiz.q1_crm, F.data.startswith("quiz_crm_"))
async def quiz_process_crm(callback: CallbackQuery, state: FSMContext) -> None:
    """Save CRM answer, move to Q2 — goal."""
    has_crm = callback.data == "quiz_crm_yes"
    await state.update_data(has_crm=has_crm)
    await state.set_state(TariffQuiz.q2_goal)
    await callback.answer()
    await callback.message.edit_text(QUIZ_Q2_GOAL, reply_markup=quiz_goal_kb())


# --- Q2: Goal answer ---

@router.callback_query(TariffQuiz.q2_goal, F.data.startswith("quiz_goal_"))
async def quiz_process_goal(callback: CallbackQuery, state: FSMContext) -> None:
    """Save goal, branch to Q3 or skip straight to result for 'turnkey'."""
    goal = callback.data.replace("quiz_goal_", "")  # automate | grow | turnkey
    await state.update_data(goal=goal)
    await callback.answer()

    if goal == "turnkey":
        # Skip Q3 — go directly to result
        await _show_quiz_result(callback, state)
    elif goal == "grow":
        # Q3 — do clients get lost?
        await state.set_state(TariffQuiz.q3_detail)
        await callback.message.edit_text(
            QUIZ_Q3_LOSE_CLIENTS, reply_markup=quiz_lose_clients_kb()
        )
    else:
        # goal == "automate" → Q3 — do you reply manually?
        await state.set_state(TariffQuiz.q3_detail)
        await callback.message.edit_text(
            QUIZ_Q3_MANUAL, reply_markup=quiz_manual_kb()
        )


# --- Q3: Detail answer ---

@router.callback_query(TariffQuiz.q3_detail, F.data.startswith("quiz_detail_"))
async def quiz_process_detail(callback: CallbackQuery, state: FSMContext) -> None:
    """Save Q3 detail, show result."""
    detail = callback.data.replace("quiz_detail_", "")
    await state.update_data(detail=detail)
    await callback.answer()
    await _show_quiz_result(callback, state)


# --- Result display with "thinking" delay ---

async def _show_quiz_result(callback: CallbackQuery, state: FSMContext) -> None:
    """Show 'thinking' message, wait 1.5s, then show personalized result."""
    data = await state.get_data()
    await state.clear()

    # Show "thinking" effect
    await callback.message.edit_text(QUIZ_THINKING)
    await asyncio.sleep(1.5)

    # Build personalized recommendation
    result_text, _tariff = build_quiz_result(
        has_crm=data.get("has_crm", False),
        goal=data.get("goal", "grow"),
        detail=data.get("detail"),
    )

    await callback.message.edit_text(result_text, reply_markup=quiz_result_kb())
