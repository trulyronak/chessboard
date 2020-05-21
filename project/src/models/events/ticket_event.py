from __future__ import annotations

from ....setup import db
from enum import Enum
from ...utils.time import TimeUtil
from ..user import User
# from ..ticket import Ticket
# from ..course import Course


class EventType(Enum):
    """
    All the event that can happen to a ticket with the \
        following options --> database value:\n
    CREATED --> 0
    ACCEPTED --> 1
    RESOLVED --> 2
    UPDATED --> 3
    DEFERED --> 4
    CANCELED --> 5
    COMMENTED --> 6
    """
    CREATED = 0
    ACCEPTED = 1
    RESOLVED = 2
    UPDATED = 3
    DEFERRED = 4
    CANCELED = 5
    COMMENTED = 6


class TicketEvent(db.Model):
    """
    The event happened on ticket.\n
    Fields:\n
    id --> The id of the ticket, unique primary key.\n
    event_type --> The type of this event.\n
    ticket_id --> The ticket associated with this event, forien key.\n
    message --> The message associated with this event, nullable.\n
    is_private --> Whether this update is anonymous.\n
    user_id --> The user that created this event.\n
    timestamp --> The timestamp of this event.\n
    """
    __tablename__ = 'TicketEvent'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # need to change a name in db, since type is a presereved word in python
    event_type = db.Column(db.Integer, nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'),
                          nullable=False)
    message = db.Column(db.String(255), nullable=True)
    is_private = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                          default=TimeUtil.get_current_time())

    # Getter Methods
    def is_create(self) -> bool:
        """
        Check if the event type is create.\n
        Return:\n
        Bool indicating if it its create type.\n
        """
        return self.event_type == EventType.CREATED

    def is_accepted(self) -> bool:
        """
        Check if the event type is accepted.\n
        Return:\n
        Bool indicating if it its accepted type.\n
        """
        return self.event_type == EventType.ACCEPTED

    def is_resolved(self) -> bool:
        """
        Check if the event type is resolved.\n
        Return:\n
        Bool indicating if it its resolved type.\n
        """
        return self.event_type == EventType.RESOLVED

    def is_update(self) -> bool:
        """
        Check if the event type is update.\n
        Return:\n
        Bool indicating if it its update type.\n
        """
        return self.event_type == EventType.UPDATED

    def is_deffered(self) -> bool:
        """
        Check if the event type is deffered.\n
        Return:\n
        Bool indicating if it its deffered type.\n
        """
        return self.event_type == EventType.DEFERRED

    def is_canceled(self) -> bool:
        """
        Check if the event type is canceled.\n
        Return:\n
        Bool indicating if it its canceled type.\n
        """
        return self.event_type == EventType.CANCELED

    def is_commented(self) -> bool:
        """
        Check if the event type is commented.\n
        Return:\n
        Bool indicating if it its commeneted type.\n
        """
        return self.event_type == EventType.COMMENTED

    def reveal_user(self, user: User, course: Course) -> bool:
        """
        Determine whether this event can be revealed to a user.\n
        Inputs:\n
        user --> The user object to be determined.\n
        course --> The course of this user & of this ticket is in.\b
        Return:\n
        bool value of whether this can be viewed by this user.\n
        """
        # Need methods from enrolledcourse and user.

    # Not implemnting (since not used):
    # findAllForTutor

    # Static add method
    @staticmethod
    def add_to_db(te: TicketEvent):
        """
        Add the ticket event to the database.\n
        Inputs:\n
        te --> the ticket event object created.\n
        """
        db.session.add(te)
        db.session.commit()
