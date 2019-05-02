#
# PySNMP MIB module OPTIX-SONET-LPBK-MIB-V2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-LPBK-MIB-V2
# Produced by pysmi-0.3.4 at Wed May  1 14:35:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
optixCommonSonet, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommonSonet")
MOD2Type, = mibBuilder.importSymbols("OPTIX-SONET-TC-MIB", "MOD2Type")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, MibIdentifier, Integer32, ModuleIdentity, Bits, TimeTicks, Unsigned32, Counter32, Counter64, NotificationType, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "MibIdentifier", "Integer32", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32", "Counter32", "Counter64", "NotificationType", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixSonetMaintenance = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50))
if mibBuilder.loadTexts: optixSonetMaintenance.setLastUpdated('200602231756Z')
if mibBuilder.loadTexts: optixSonetMaintenance.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: optixSonetMaintenance.setContactInfo('R&D Building Huawei Technologies Co., Ltd. Bantian, Longgang District Shenzhen, P. R. China http://www.huawei.com Zip:518129 E-mail:support@huawei.com ')
if mibBuilder.loadTexts: optixSonetMaintenance.setDescription('This module describes the Loopback interface of Huawei SONET transmit platform ')
class LpbkType(TextualConvention, Integer32):
    description = 'Enter the description for the LpbkType TEXTUAL-CONVENTION converted from type assignment.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(255, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("noloop", 255), ("terminal", 1), ("facility", 2), ("crs", 3), ("ds1feac", 4), ("ds3feac", 5), ("fac2ni", 6))

optixSonetLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10))
lpbkStateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10), )
if mibBuilder.loadTexts: lpbkStateTable.setStatus('current')
if mibBuilder.loadTexts: lpbkStateTable.setDescription('Loopback state table ')
lpbkStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1), ).setIndexNames((0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateMOD2"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateSlot"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePort"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePath"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkStateVT"))
if mibBuilder.loadTexts: lpbkStateEntry.setStatus('current')
if mibBuilder.loadTexts: lpbkStateEntry.setDescription('Loopback state entry ')
lpbkStateMOD2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 1), MOD2Type()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStateMOD2.setStatus('current')
if mibBuilder.loadTexts: lpbkStateMOD2.setDescription('The modifier that identifies the type of the facility')
lpbkStateSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStateSlot.setStatus('current')
if mibBuilder.loadTexts: lpbkStateSlot.setDescription('Slot number. This will indicate what is the slot of the object.')
lpbkStatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStatePort.setStatus('current')
if mibBuilder.loadTexts: lpbkStatePort.setDescription('Port Number. This will indicate what is the Port of the object.')
lpbkStatePath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStatePath.setStatus('current')
if mibBuilder.loadTexts: lpbkStatePath.setDescription('Path number. This will indicate what is the Path of the object.')
lpbkStateVT = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStateVT.setStatus('current')
if mibBuilder.loadTexts: lpbkStateVT.setDescription('VT path number. This will indicate what is the VT path of the object.')
lpbkStateLpbkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 6), LpbkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStateLpbkType.setStatus('current')
if mibBuilder.loadTexts: lpbkStateLpbkType.setDescription('The loopback type of the facility ')
lpbkStateTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 10, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkStateTimeout.setStatus('current')
if mibBuilder.loadTexts: lpbkStateTimeout.setDescription('The remnant time that loop-back will be released. ')
lpbkFlagTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20), )
if mibBuilder.loadTexts: lpbkFlagTable.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagTable.setDescription('Loopback Enable table')
lpbkFlagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1), ).setIndexNames((0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagMOD2"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagSlot"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPort"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPath"), (0, "OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagVT"))
if mibBuilder.loadTexts: lpbkFlagEntry.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagEntry.setDescription('Loopback Enable entry')
lpbkFlagMOD2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 1), MOD2Type()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagMOD2.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagMOD2.setDescription('The modifier that identifies the type of the facility')
lpbkFlagSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagSlot.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagSlot.setDescription('Slot number. This will indicate what is the slot of the object.')
lpbkFlagPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagPort.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagPort.setDescription('Port Number. This will indicate what is the Port of the object.')
lpbkFlagPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagPath.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagPath.setDescription('Path number. This will indicate what is the Path of the object.')
lpbkFlagVT = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagVT.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagVT.setDescription('VT path number. This will indicate what is the VT path of the object.')
lpbkFlagLpbkType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 6), LpbkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagLpbkType.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagLpbkType.setDescription('The loopback type of the facility ')
lpbkFlagEnFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagEnFlag.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagEnFlag.setDescription('T1 or T3 remote loop-back enable flag ')
lpbkFlagTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 10, 20, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lpbkFlagTimeout.setStatus('current')
if mibBuilder.loadTexts: lpbkFlagTimeout.setDescription('The automatic release time of loopback.')
optixSonetMaintenanceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11))
optixSonetMaintenanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 1))
currentObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 1, 1)).setObjects(("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateMOD2"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateSlot"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePort"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStatePath"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateVT"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateLpbkType"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkStateTimeout"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagMOD2"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagSlot"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPort"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagPath"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagVT"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagLpbkType"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagEnFlag"), ("OPTIX-SONET-LPBK-MIB-V2", "lpbkFlagTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    currentObjectGroup = currentObjectGroup.setStatus('current')
if mibBuilder.loadTexts: currentObjectGroup.setDescription('Enter the description of the created OBJECT-GROUP.')
optixSonetMaintenanceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 2))
basicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 50, 11, 2, 1)).setObjects(("OPTIX-SONET-LPBK-MIB-V2", "currentObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    basicCompliance = basicCompliance.setStatus('current')
if mibBuilder.loadTexts: basicCompliance.setDescription('Enter the description of the created MODULE-COMPLIANCE.')
mibBuilder.exportSymbols("OPTIX-SONET-LPBK-MIB-V2", lpbkFlagTable=lpbkFlagTable, lpbkFlagEntry=lpbkFlagEntry, lpbkStateTimeout=lpbkStateTimeout, optixSonetMaintenanceGroups=optixSonetMaintenanceGroups, optixSonetMaintenance=optixSonetMaintenance, lpbkFlagPath=lpbkFlagPath, lpbkFlagMOD2=lpbkFlagMOD2, lpbkStateSlot=lpbkStateSlot, lpbkFlagPort=lpbkFlagPort, lpbkFlagSlot=lpbkFlagSlot, lpbkStatePath=lpbkStatePath, optixSonetMaintenanceConformance=optixSonetMaintenanceConformance, lpbkStatePort=lpbkStatePort, lpbkStateTable=lpbkStateTable, LpbkType=LpbkType, currentObjectGroup=currentObjectGroup, lpbkFlagLpbkType=lpbkFlagLpbkType, optixSonetLoopback=optixSonetLoopback, lpbkStateVT=lpbkStateVT, lpbkStateEntry=lpbkStateEntry, lpbkStateLpbkType=lpbkStateLpbkType, lpbkStateMOD2=lpbkStateMOD2, lpbkFlagEnFlag=lpbkFlagEnFlag, lpbkFlagTimeout=lpbkFlagTimeout, PYSNMP_MODULE_ID=optixSonetMaintenance, optixSonetMaintenanceCompliances=optixSonetMaintenanceCompliances, lpbkFlagVT=lpbkFlagVT, basicCompliance=basicCompliance)