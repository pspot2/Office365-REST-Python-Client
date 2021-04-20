from office365.entity import Entity


class CalendarPermission(Entity):
    """
    The permissions of a user with whom the calendar has been shared or delegated in an Outlook client.

    Get, update, and delete of calendar permissions is supported on behalf of only the calendar owner.

    Getting the calendar permissions of a calendar on behalf of a sharee or delegate returns
    an empty calendar permissions collection.

    Once a sharee or delegate has been set up for a calendar, you can update only the role property to change
    the permissions of a sharee or delegate. You cannot update the allowedRoles, emailAddress, isInsideOrganization,
    or isRemovable property. To change these properties, you should delete the corresponding calendarPermission
    object and create another sharee or delegate in an Outlook client.

    """
    pass
