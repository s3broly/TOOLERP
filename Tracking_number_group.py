class TrackingNumberGroup:
    def __init__(self, isactivatedforsales, isactivatedforkanban, 
                 isnumbersequencenumberincluded, willphysicalupdateassignnumber, 
                 isactivatedforproduction, groupname, numbersequencecode, 
                 numbersequencescopedataarea, isreferencenumberincluded, groupcode, 
                 islotidincluded, inventoryquantitytreshold, isexpecteddateincluded, 
                 isnumbermanuallyallocated, isonlyforinventorytransactions, 
                 isactivatedforpurchase, isactivatedforinventory ):
        self.groupname= groupname
        self.groupcode = groupcode
        self.isactivatedforsales = isactivatedforsales
        self.isactivatedforkanban = isactivatedforkanban
        self.isnumbersequencenumberincluded = isnumbersequencenumberincluded
        self.willphysicalupdateassignnumber = willphysicalupdateassignnumber
        self.isactivatedforproduction = isactivatedforproduction
        self.numbersequencecode = numbersequencecode
        self.numbersequencescopedataarea = numbersequencescopedataarea
        self.isreferencenumberincluded = isreferencenumberincluded
        self.islotidincluded = islotidincluded
        self.inventoryquantitytreshold = inventoryquantitytreshold
        self.isexpecteddateincluded = isexpecteddateincluded
        self.isnumbermanuallyallocated = isnumbermanuallyallocated
        self.isonlyforinventorytransactions = isonlyforinventorytransactions
        self.isactivatedforpurchase = isactivatedforpurchase
        self.isactivatedforinventory = isactivatedforinventory

        