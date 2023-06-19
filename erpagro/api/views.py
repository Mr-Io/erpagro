from django.contrib.auth.decorators import permission_required, login_required

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from packaging.models import Packaging
from product.models import AgrofoodType
from purchases.models import Supplier, CarrierAgent, Charge
from quality.models import Land, Warehouse


#################### AGROFOODTYPE ####################
class PackagingTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = ["pk", "name"]

#################### AGROFOODTYPE ####################
class AgrofoodTypeListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="__str__")
    class Meta:
        model = AgrofoodType
        fields = ["pk", "name"]

class AgrofoodTypeDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="__str__")
    packaging = PackagingTypeListSerializer(read_only=True)
    class Meta:
        model = AgrofoodType
        fields = ["name", "packaging"]


#################### WAREHOUSE ####################
class WarehouseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["pk", "name"]

class WarehouseDetailSerializer(serializers.ModelSerializer):
    agrofoodtypes = AgrofoodTypeListSerializer(many=True, read_only=True)
    class Meta:
        model = Warehouse
        fields = ["name", "agrofoodtypes"]


#################### CARRIERAGENT ####################
class CarrierAgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierAgent
        fields = ["pk", "name", "carrier_price"]

class CarrierAgentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierAgent
        fields = ["pk", "name", "carrier_price"]


#################### CHARGE ####################
class ChargeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charge
        fields = ["pk", "name"]

#################### SUPPLIER ####################
class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["pk", "name"]

class LandExpandSerializer(serializers.ModelSerializer):
    warehouse_set = WarehouseListSerializer(many=True, read_only=True)
    class Meta:
        model=Land
        fields = ["name", "warehouse_set"]

class SupplierDetailSerializer(serializers.ModelSerializer):
    land_set = LandExpandSerializer(many=True, read_only=True)
    carrier = CarrierAgentListSerializer(read_only=True)
    charge = ChargeListSerializer(read_only=True)
    class Meta:
        model = Supplier
        fields = ["name", "cif", "mobile", "carrier", "charge", "land_set"]

######################## VIEWS ########################

@api_view(["GET"])
@permission_required(["purchases.view_supplier"], raise_exception=True)
def supplier_list(request):
    if request.method == "GET":
        suppliers = Supplier.objects.all()
        serializer = SupplierListSerializer(suppliers, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def supplier_detail(request, pk):
    if not request.user.is_authenticated:
        return Response({"detail": "Permisos Insuficientes"}, status=status.HTTP_403_FORBIDDEN)
    try:
        supplier = Supplier.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        if request.user.has_perms(["purchases.view_supplier", "quality.view_land", "quality.view_warehouse"]) or supplier.is_this_user(request.user):
            serializer = SupplierDetailSerializer(supplier)
            return Response(serializer.data)
        return Response({"detail": "Permisos Insuficientes"}, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET"])
@permission_required(["quality.view_warehouse"], raise_exception=True)
def warehouse_detail(request, pk):
    try:
        warehouse = Warehouse.objects.get(pk=pk)
    except Warehouse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WarehouseDetailSerializer(warehouse)
        return Response(serializer.data)


@api_view(["GET"])
@permission_required(["product.view_agrofoodtype"], raise_exception=True)
def agrofoodtype_detail(request, pk):
    try:
        agrofoodtype = AgrofoodType.objects.get(pk=pk)
    except AgrofoodType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AgrofoodTypeDetailSerializer(agrofoodtype)
        return Response(serializer.data)


@api_view(["GET"])
@permission_required(["product.view_agrofoodtype"], raise_exception=True)
def carrier_detail(request, pk):
    try:
        carrier = CarrierAgent.objects.get(pk=pk)
    except CarrierAgent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CarrierAgentDetailSerializer(carrier)
        return Response(serializer.data)