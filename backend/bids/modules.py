from fastapi import HTTPException, status

from common.db import Bid, Lot, UserStatus
from common.responses import NotEnoughRightsResponse
from .schemas import ExistsBiggerBidResponse, BidNotFoundResponse, CantWithdrawBidResponse, BidAlreadyWithdrawnResponse


def can_withdraw_bid(bid: Bid) -> bool:
    lot = bid.lot
    if bid.is_withdrawn:
        return False
    if lot.is_canceled and bid.id == lot.win_bid_id:
        return False
    if not lot.is_canceled and lot.max_bid == bid.amount:
        return False
    return True


def raise_if_bid_not_exists(bid: Bid) -> None:
    if bid is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=BidNotFoundResponse().detail
        )


def raise_if_no_access_to_edit_bid(
        bid: Bid,
        user_id: int,
        user_status: UserStatus
) -> None:
    if bid.owner_id != user_id and user_status != UserStatus.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=NotEnoughRightsResponse().detail
        )


def raise_if_exists_bigger_bid(
        lot: Lot,
        amount: int
) -> None:
    if lot.max_bid >= amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ExistsBiggerBidResponse().detail
        )


def raise_if_cant_withdraw_bid(bid: Bid) -> None:
    if not can_withdraw_bid(bid):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=CantWithdrawBidResponse().detail
        )


def raise_bid_already_withdrawn() -> None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=BidAlreadyWithdrawnResponse().detail
    )
