from django.shortcuts import render, redirect
from dashboard.models import MessAnnouncements
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from mess.models import MessLeave, MessRefund, OrderListMess, MessItems
#from .forms import MessAnnouncementForm, AddAnnouncementForm
from django.http import HttpResponse
import datetime
import time
from django.template.loader import render_to_string
from orders.models import ManualOrder
from .forms import AddItemForm, AddAnnouncementForm, MessAnnouncementForm

def mess_admin_index(request):
    return render(request, 'mess_admin/index.html')

def mess_admin_dashboard(request):
    mess_announcements = list(MessAnnouncements.objects.all())
    mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)
    mess_leave = list(MessLeave.objects.all())
    mess_leave.sort(key = lambda a: a.timestamp, reverse = True)
    mess_refund = list(MessRefund.objects.all())
    mess_refund.sort(key = lambda a: a.timestamp, reverse = True)
    mess_items = list(MessItems.objects.all())
    mess_items.sort(key = lambda a: a.timestamp, reverse = True)
    mess_order = list(OrderListMess.objects.all())
    mess_order.sort(key = lambda a: a.timestamp, reverse = True)    
    return render(request, 'mess_admin/mess_admin_dashboard.html', {'mess_announcements': mess_announcements,'mess_leave':mess_leave, 'mess_refund': mess_refund, 'mess_order': mess_order, 'mess_items': mess_items
    })

def mess_leave_show(request, pk):
    leave = get_object_or_404(MessLeave, pk = pk)
    return render(request, 'mess_admin/leaves.html', {'leave': leave})
    
def mess_refund_show(request, pk):
    refund = get_object_or_404(MessRefund, pk = pk)
    return render(request, 'mess_admin/refunds.html', {'refund': refund})
    

# announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
# announcement=forms.CharField(label='announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
# timestamp=forms.DateField(label='timestamp',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
# modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))

def announcement_delete(request, id):
    print(id)
    announcement = MessAnnouncements.objects.get(pk=id)
    announcement.delete()
    return redirect('mess_admin:mess_admin_dashboard')

def leave_delete(request, id):
    leave = MessLeave.objects.get(pk=id)
    leave.delete()
    return redirect('mess_admin:mess_admin_dashboard')
    
def refund_delete(request, id):
    refund = MessRefund.objects.get(pk=id)
    refund.delete()
    return redirect('mess_admin:mess_admin_dashboard')


def item_delete(request, id):
    item = MessItems.objects.get(pk = id)
    item.delete()
    return redirect('mess_admin:mess_admin_dashboard')
    

def order_delete(request, id):
    order = OrderListMess.objects.get(pk = id)
    order.delete()
    return redirect('mess_admin:mess_admin_dashboard')


def announcement_edit(request, id):
    Mess_announcement = MessAnnouncements.objects.get(pk=id)
    Mess_announcement_form = AddAnnouncementForm(initial = {
    'announcement_title': Mess_announcement.announcement_title,
    'announcement': Mess_announcement.announcement,
    })
    print(Mess_announcement_form)
    return render(request, 'mess_admin/edit_announcements.html', {
    'form': Mess_announcement_form,
    'id': id,
})

def item_edit(request, id):
    Mess_item = MessItems.objects.get(pk=id)
    Mess_item_form = AddItemForm(initial = {
    'item_name': Mess_item.item_name,
    'quantity': Mess_item.quantity,
    'cost': Mess_item.cost
    })
    #print(Mess_announcement_form)
    return render(request, 'mess_admin/edit_items.html', {
    'form': Mess_item_form,
    'id': id,
})
def add_announcement(request):
    if request.method == 'GET':
        add_announcement_form = AddAnnouncementForm()
        return HttpResponse(render_to_string('mess_admin/add.html',context={
        'add_announcement_form': add_announcement_form,
        }))

def add_item(request):
    if request.method == 'GET':
        add_item_form = AddItemForm()
        return HttpResponse(render_to_string('mess_admin/addI.html',context={'add_item_form': add_item_form,}))

def add_announcement_url(request):
    if request.method == 'POST':
        form = AddAnnouncementForm(request.POST)
        if form.is_valid():
            add_announcement_form=form.save(commit=False)
            add_announcement_form.timestamp=datetime.datetime.now()
            add_announcement_form.created_at=datetime.datetime.now().date()
            add_announcement_form.modified_at = datetime.datetime.now().date()
            add_announcement_form.created_by=request.user.username
            add_announcement_form.modified_by=request.user.username
            add_announcement_form.save()

            return redirect('mess_admin:mess_admin_dashboard')
    print(form.errors)

def add_item_url(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            add_item_form=form.save(commit=False)
            add_item_form.timestamp=datetime.datetime.now()
            add_item_form.created_at=datetime.datetime.now().date()
            add_item_form.modified_at = datetime.datetime.now().date()
            add_item_form.created_by=request.user.username
            add_item_form.modified_by=request.user.username
            add_item_form.save()
            return redirect('mess_admin:mess_admin_dashboard')

def save_edit_changes(request, id):
    if request.method == 'POST':
        try:
            announcement = MessAnnouncements.objects.get(pk=id)
        except MessAnnouncements.DoesNotExist:
            announcement = None
        if announcement is not None:
            announcement_title = request.POST.get('announcement_title')
            announcement_body = request.POST.get('announcement')
            flag = 0
            if announcement_title != announcement.announcement_title:
                announcement.announcement_title = announcement_title
                flag = 1
                announcement.announcement = announcement_body
                announcement.timestamp=datetime.datetime.now()
                announcement.modified_at = datetime.datetime.now().date()
                announcement.modified_by=request.user.username
            if announcement_body != announcement.announcement:
                announcement.announcement = announcement_body
                if flag == 0:
                    announcement.timestamp=datetime.datetime.now()
                    announcement.modified_at = datetime.datetime.now().date()
                    announcement.modified_by=request.user.username
            announcement.save()
        return redirect('mess_admin:mess_admin_dashboard')
    print(request.method)

def save_item_changes(request, id):
    if request.method == 'POST':
        try:
            Item = MessItems.objects.get(pk=id)
        except MessItems.DoesNotExist:
            Item = None
        if Item is not None:
            Item_name = request.POST.get('item_name')
            Item_quantity = request.POST.get('quantity')
            Item_cost = request.POST.get('cost')
            flag = 0
            if Item_name != Item.item_name or Item_quantity != Item.quantity or Item_cost != Item.cost:
                Item.item_name = Item_name
                Item.quantity = Item_quantity
                Item.cost = Item_cost
                Item.timestamp=datetime.datetime.now()
                Item.modified_at = datetime.datetime.now().date()
                Item.modified_by=request.user.username
                Item.save()
                print("THE FORM WAS SAVED")
        return redirect('mess_admin:mess_admin_dashboard')
    print(request.method)
    print("HERE")
"""
def manual_orders(request):
    manual_orders = ManualOrder.objects.all()
    length = len(manual_orders)
    return HttpResponse(render_to_string('Mess_admin/manual_order.html',context={
    'manual_orders': manual_orders,
    'len': length,
    }))

def add_item(request):
    if request.method == 'POST':
        add_item_form = AddItemForm(data = request.POST)
        if add_item_form.is_valid():
            form = add_item_form.save(commit = False)
            form.item_type = 'Others'
            form.timestamp=datetime.datetime.now()
            form.created_at = datetime.datetime.now().date()
            # print(form.created_at)
            # print('hi')
            form.modified_at = datetime.datetime.now().date()
            form.modified_by = request.user.username
            form.created_by = request.user.username
            print('hi')
            form.save()
            print('done')
        return redirect('Mess_admin:Mess_admin_dashboard')
    else:
        item_form = AddItemForm()
        return HttpResponse(render_to_string('Mess_admin/item_form.html',context={
        'form': item_form,
        }))
"""