from django.urls import path

from app.views import Index, ReportDetail, ReportAdd, Expense_add, Add, VsIndex

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path("report/<int:id>", ReportDetail.as_view(), name='report'),
    path("report/add/<int:id>", ReportAdd.as_view(), name='reportadd'),
    path("expense/add/<int:id>", Expense_add.as_view(), name='expenseadd'),
    path("add", Add.as_view(), name='add'),
    path("vcindex", VsIndex.as_view(), name='vcindex'),
]