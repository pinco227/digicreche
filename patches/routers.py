from rest_framework import routers


class DefaultRouter(routers.DefaultRouter):
    """
    CREDIT: https://stackoverflow.com/questions/31483282/
    Extends `DefaultRouter` class to add a method for extending url routes
    from another router.
    """

    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)
