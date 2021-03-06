#
# PySNMP MIB module ASCEND-MIBBRILT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBBRILT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter64, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibbRILtProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 27))
mibbRILtProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 27, 1), )
if mibBuilder.loadTexts: mibbRILtProfileTable.setStatus('mandatory')
mibbRILtProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1), ).setIndexNames((0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Shelf-o"), (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Slot-o"), (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-Item-o"))
if mibBuilder.loadTexts: mibbRILtProfileEntry.setStatus('mandatory')
bRILtProfile_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 1), Integer32()).setLabel("bRILtProfile-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_Shelf_o.setStatus('mandatory')
bRILtProfile_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 2), Integer32()).setLabel("bRILtProfile-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_Slot_o.setStatus('mandatory')
bRILtProfile_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 3), Integer32()).setLabel("bRILtProfile-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_Item_o.setStatus('mandatory')
bRILtProfile_ProfileNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 4), Integer32()).setLabel("bRILtProfile-ProfileNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_ProfileNumber.setStatus('mandatory')
bRILtProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 5), DisplayString()).setLabel("bRILtProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_Name.setStatus('mandatory')
bRILtProfile_LineInterface_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("bRILtProfile-LineInterface-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_Enabled.setStatus('mandatory')
bRILtProfile_LineInterface_AnswerNumber1 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 7), DisplayString()).setLabel("bRILtProfile-LineInterface-AnswerNumber1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_AnswerNumber1.setStatus('mandatory')
bRILtProfile_LineInterface_AnswerNumber2 = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 8), DisplayString()).setLabel("bRILtProfile-LineInterface-AnswerNumber2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_AnswerNumber2.setStatus('mandatory')
bRILtProfile_LineInterface_ClockSource = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("eligible", 1), ("notEligible", 2)))).setLabel("bRILtProfile-LineInterface-ClockSource").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ClockSource.setStatus('mandatory')
bRILtProfile_LineInterface_IdslBandwidth = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idsl128", 1), ("idsl144", 2)))).setLabel("bRILtProfile-LineInterface-IdslBandwidth").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_IdslBandwidth.setStatus('mandatory')
bRILtProfile_LineInterface_Gr303Crv = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 11), Integer32()).setLabel("bRILtProfile-LineInterface-Gr303Crv").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_Gr303Crv.setStatus('mandatory')
bRILtProfile_LineInterface_Gr303InterfaceGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 12), Integer32()).setLabel("bRILtProfile-LineInterface-Gr303InterfaceGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_Gr303InterfaceGroup.setStatus('mandatory')
bRILtProfile_LineInterface_IgnoreLineup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("systemDefined", 1), ("no", 2), ("yes", 3)))).setLabel("bRILtProfile-LineInterface-IgnoreLineup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_IgnoreLineup.setStatus('mandatory')
bRILtProfile_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("bRILtProfile-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_PhysicalAddress_Shelf.setStatus('mandatory')
bRILtProfile_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("bRILtProfile-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_PhysicalAddress_Slot.setStatus('mandatory')
bRILtProfile_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 15), Integer32()).setLabel("bRILtProfile-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_PhysicalAddress_ItemNumber.setStatus('mandatory')
bRILtProfile_SwitchType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 31, 11, 12, 13, 14, 32, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30))).clone(namedValues=NamedValues(("attPri", 1), ("ntiPri", 2), ("globandPri", 3), ("japanPri", 4), ("vn3Pri", 5), ("onetr6Pri", 6), ("net5Pri", 7), ("danishPri", 8), ("australPri", 9), ("natIsdn2Pri", 10), ("taiwanPri", 31), ("isdxDpnss", 11), ("islxDpnss", 12), ("mercuryDpnss", 13), ("dass2", 14), ("btSs7", 32), ("unknownBri", 15), ("att5essBri", 16), ("dms100Nt1Bri", 17), ("nisdn1Bri", 18), ("vn2Bri", 19), ("btnr191Bri", 20), ("net3Bri", 21), ("ptpNet3Bri", 22), ("kddBri", 23), ("belgianBri", 24), ("australBri", 25), ("swissBri", 26), ("german1tr6Bri", 27), ("dutch1tr6Bri", 28), ("switchCas", 29), ("idslPtpBri", 30)))).setLabel("bRILtProfile-SwitchType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_SwitchType.setStatus('mandatory')
bRILtProfile_SparingMode = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("manual", 2), ("automatic", 3)))).setLabel("bRILtProfile-SparingMode").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_SparingMode.setStatus('mandatory')
bRILtProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("bRILtProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_Action_o.setStatus('mandatory')
mibbRILtProfile_LineInterface_ChannelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 27, 2), ).setLabel("mibbRILtProfile-LineInterface-ChannelConfigTable")
if mibBuilder.loadTexts: mibbRILtProfile_LineInterface_ChannelConfigTable.setStatus('mandatory')
mibbRILtProfile_LineInterface_ChannelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1), ).setLabel("mibbRILtProfile-LineInterface-ChannelConfigEntry").setIndexNames((0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Shelf-o"), (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Slot-o"), (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Item-o"), (0, "ASCEND-MIBBRILT-MIB", "bRILtProfile-LineInterface-ChannelConfig-Index-o"))
if mibBuilder.loadTexts: mibbRILtProfile_LineInterface_ChannelConfigEntry.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 1), Integer32()).setLabel("bRILtProfile-LineInterface-ChannelConfig-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_Shelf_o.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 2), Integer32()).setLabel("bRILtProfile-LineInterface-ChannelConfig-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_Slot_o.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 3), Integer32()).setLabel("bRILtProfile-LineInterface-ChannelConfig-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_Item_o.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 4), Integer32()).setLabel("bRILtProfile-LineInterface-ChannelConfig-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_Index_o.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_ChannelUsage = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("unusedChannel", 1), ("switchedChannel", 2), ("nailed64Channel", 3), ("dChannel", 4), ("nfasPrimaryDChannel", 5), ("nfasSecondaryDChannel", 6), ("semiPermChannel", 7), ("ss7SignalingChannel", 8)))).setLabel("bRILtProfile-LineInterface-ChannelConfig-ChannelUsage").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_ChannelUsage.setStatus('mandatory')
bRILtProfile_LineInterface_ChannelConfig_NailedGroup = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 27, 2, 1, 6), Integer32()).setLabel("bRILtProfile-LineInterface-ChannelConfig-NailedGroup").setMaxAccess("readwrite")
if mibBuilder.loadTexts: bRILtProfile_LineInterface_ChannelConfig_NailedGroup.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBBRILT-MIB", bRILtProfile_PhysicalAddress_Shelf=bRILtProfile_PhysicalAddress_Shelf, mibbRILtProfileTable=mibbRILtProfileTable, mibbRILtProfile=mibbRILtProfile, bRILtProfile_LineInterface_IgnoreLineup=bRILtProfile_LineInterface_IgnoreLineup, bRILtProfile_LineInterface_ChannelConfig_NailedGroup=bRILtProfile_LineInterface_ChannelConfig_NailedGroup, bRILtProfile_Slot_o=bRILtProfile_Slot_o, mibbRILtProfile_LineInterface_ChannelConfigEntry=mibbRILtProfile_LineInterface_ChannelConfigEntry, bRILtProfile_LineInterface_ChannelConfig_Index_o=bRILtProfile_LineInterface_ChannelConfig_Index_o, bRILtProfile_Name=bRILtProfile_Name, bRILtProfile_Action_o=bRILtProfile_Action_o, bRILtProfile_LineInterface_IdslBandwidth=bRILtProfile_LineInterface_IdslBandwidth, bRILtProfile_PhysicalAddress_ItemNumber=bRILtProfile_PhysicalAddress_ItemNumber, mibbRILtProfile_LineInterface_ChannelConfigTable=mibbRILtProfile_LineInterface_ChannelConfigTable, bRILtProfile_LineInterface_AnswerNumber1=bRILtProfile_LineInterface_AnswerNumber1, bRILtProfile_LineInterface_Gr303InterfaceGroup=bRILtProfile_LineInterface_Gr303InterfaceGroup, bRILtProfile_LineInterface_ChannelConfig_Item_o=bRILtProfile_LineInterface_ChannelConfig_Item_o, bRILtProfile_SparingMode=bRILtProfile_SparingMode, bRILtProfile_LineInterface_Enabled=bRILtProfile_LineInterface_Enabled, bRILtProfile_PhysicalAddress_Slot=bRILtProfile_PhysicalAddress_Slot, bRILtProfile_LineInterface_ChannelConfig_Slot_o=bRILtProfile_LineInterface_ChannelConfig_Slot_o, bRILtProfile_LineInterface_ClockSource=bRILtProfile_LineInterface_ClockSource, bRILtProfile_LineInterface_ChannelConfig_ChannelUsage=bRILtProfile_LineInterface_ChannelConfig_ChannelUsage, bRILtProfile_LineInterface_ChannelConfig_Shelf_o=bRILtProfile_LineInterface_ChannelConfig_Shelf_o, bRILtProfile_Shelf_o=bRILtProfile_Shelf_o, mibbRILtProfileEntry=mibbRILtProfileEntry, bRILtProfile_LineInterface_AnswerNumber2=bRILtProfile_LineInterface_AnswerNumber2, bRILtProfile_ProfileNumber=bRILtProfile_ProfileNumber, bRILtProfile_LineInterface_Gr303Crv=bRILtProfile_LineInterface_Gr303Crv, DisplayString=DisplayString, bRILtProfile_SwitchType=bRILtProfile_SwitchType, bRILtProfile_Item_o=bRILtProfile_Item_o)
