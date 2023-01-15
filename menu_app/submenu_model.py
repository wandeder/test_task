from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from menu_app.menu_model import Menu
    from menu_app.dish_model import Dish


class SubmenuBase(SQLModel):
    title: str = Field(index=True)
    description: str
    menu_id: Optional[int] = Field(default=None, foreign_key="menu.id")
    dishes_count: Optional[int] = None


class Submenu(SubmenuBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    menu: Optional["Menu"] = Relationship(back_populates="submenus")
    dishes: List["Dish"] = Relationship(back_populates="submenu")


class SubmenuCreate(SubmenuBase):
    pass


class SubmenuRead(SubmenuBase):
    id: int


class SubmenuUpdate(SQLModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None