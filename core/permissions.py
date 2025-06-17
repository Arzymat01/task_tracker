from rest_framework.permissions import BasePermission


class IsWorker(BasePermission):
    """
    Жумушчу (Worker) колдонуучулар үчүн уруксат.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'worker'


class IsDispatcher(BasePermission):
    """
    Диспетчер (Dispatcher) колдонуучулар үчүн уруксат.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'dispatcher'


class IsSupervisor(BasePermission):
    """
    Супервайзер (Supervisor) колдонуучулар үчүн уруксат.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'supervisor'
