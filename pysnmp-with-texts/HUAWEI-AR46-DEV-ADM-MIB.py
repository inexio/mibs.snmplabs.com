#
# PySNMP MIB module HUAWEI-AR46-DEV-ADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-AR46-DEV-ADM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
mlsr, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "mlsr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, TimeTicks, ObjectIdentity, iso, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ModuleIdentity, IpAddress, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "TimeTicks", "ObjectIdentity", "iso", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aR46_E200 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20)).setLabel("aR46-E200")
if mibBuilder.loadTexts: aR46_E200.setLastUpdated('200310221643Z')
if mibBuilder.loadTexts: aR46_E200.setOrganization('8060 Team Huawei Tech. ')
if mibBuilder.loadTexts: aR46_E200.setContactInfo('liuaki 03198/huawei@huawei.')
if mibBuilder.loadTexts: aR46_E200.setDescription('This MIB is designed and realized by ChenWenjun for 8060 on March 27, 2003. Modified by Liukai on Oct 22, 2003')
hw8060DevObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1))
hw8060FrameTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1), )
if mibBuilder.loadTexts: hw8060FrameTable.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameTable.setDescription('Frame table.')
hw8060FrameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060FrameIndex"))
if mibBuilder.loadTexts: hw8060FrameEntry.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameEntry.setDescription('Frame table entry.')
hw8060FrameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060FrameIndex.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameIndex.setDescription('This variable indicates the index of the frame')
hw8060FrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060FrameType.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameType.setDescription('This variable indicates the type of the frame')
hw8060FrameDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8060FrameDesc.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameDesc.setDescription('This variable indicates the description of the frame')
hw8060FrameSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060FrameSlotNumber.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameSlotNumber.setDescription('This variable indicates the total number of slots in the frame')
hw8060FrameAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060FrameAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060FrameAdminStatus.setDescription('This variable indicates the administration status of the frame')
hw8060SlotTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2), )
if mibBuilder.loadTexts: hw8060SlotTable.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotTable.setDescription('Slot table.')
hw8060SlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060SlotIndex"))
if mibBuilder.loadTexts: hw8060SlotEntry.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotEntry.setDescription('Slot table entry.')
hw8060SlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotIndex.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotIndex.setDescription('This variable indicates the index of the current slot')
hw8060SlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233))).clone(namedValues=NamedValues(("unavailable", 1), ("as", 2), ("ss", 3), ("bi", 4), ("e12", 5), ("e14", 6), ("fe1", 7), ("e1", 8), ("fe2", 9), ("vi2", 11), ("vi4", 12), ("vi30", 13), ("s1b", 14), ("sa2", 15), ("as16", 16), ("new8as", 17), ("lsa", 18), ("fxs2", 19), ("fxo2", 20), ("em2", 21), ("fxs4", 22), ("fxo4", 23), ("em4", 24), ("sab", 25), ("e1vi", 26), ("am12", 27), ("am6", 28), ("ndec", 29), ("newsa2", 30), ("aux", 31), ("console", 32), ("sic-wan", 33), ("sic-1fe", 34), ("sic-1sa", 35), ("sic-3as", 36), ("sic-1e1", 37), ("sic-1t1", 38), ("sic-1bu", 39), ("sic-2bu", 40), ("sic-1bs", 41), ("sic-2bs", 42), ("sic-1am", 43), ("sic-2am", 44), ("sic-1em", 45), ("sic-2em", 46), ("sic-1fxs", 47), ("sic-2fxs", 48), ("sic-1fxo", 49), ("sic-2fxo", 50), ("fcm6", 51), ("sa8", 52), ("t11", 53), ("t12", 54), ("t14", 55), ("t1vi", 56), ("fcm4", 57), ("fcm2", 58), ("rtb21ce3", 59), ("ame6", 60), ("ame12", 61), ("e11-f", 65), ("e12-f", 66), ("e14-f", 67), ("t11-f", 68), ("t12-f", 69), ("t14-f", 70), ("e11-f-17", 71), ("t11-f-17", 72), ("rtb21ct3", 73), ("atmadsl1", 74), ("atmadsl2", 75), ("atm155m", 76), ("ase8", 77), ("ase16", 78), ("sae4", 79), ("sae2", 80), ("atmshdsl1", 90), ("atmshdsl2", 91), ("atmshdsl4", 92), ("atm25m", 93), ("atme3", 94), ("atmt3", 95), ("xdsl-fec", 96), ("xdsl-adsl", 97), ("xdsl-gshdsl", 98), ("xdsl-bri", 99), ("xdsl-scc", 100), ("ge1", 101), ("pos155m", 102), ("cpos", 103), ("fe1op", 104), ("sae8", 105), ("atm155m-mm", 106), ("atm155m-sm", 107), ("atm155m-sml", 108), ("fe1op-sfx", 109), ("fe1op-mfx", 110), ("cpos-t1", 111), ("ge1-op", 112), ("ge2-op", 113), ("ge2", 114), ("fix-1wan", 115), ("fix-1sae", 116), ("cavium", 117), ("sic-1Eth", 118), ("atm1ADSLI", 119), ("atm2ADSLI", 120), ("fix-e11", 121), ("fix-t11", 122), ("e18-75", 123), ("e18-120", 124), ("t18", 125), ("sic-1vifxs", 126), ("sic-1vifxo", 127), ("sic-2vifxs", 128), ("sic-2vifxo", 129), ("xdsl-fec-new", 130), ("xdsl-sa", 131), ("bs4", 132), ("ima-8e175", 133), ("ima-8e1120", 134), ("ima-4e175", 135), ("ima-4e1120", 136), ("ima-8t1", 137), ("ima-4t1", 138), ("sic-1t1f", 139), ("sic-1e1f", 140), ("atm1shdsl4wire", 151), ("atmIma4shdsl", 152), ("ls4", 153), ("ls8", 154), ("ls16", 155), ("sic-adls2plus-isdn", 156), ("sic-adls2plus-pots", 157), ("ft3", 158), ("ce32", 159), ("bsv2", 160), ("bsv4", 161), ("rpu", 162), ("erpu", 163), ("fe18-75", 220), ("fe18-120", 221), ("ft18", 222), ("cf-card", 223), ("bsv2-v2", 224), ("e1vi1-v2", 225), ("e1vi2", 226), ("t1vi1-v2", 227), ("t1vi2", 228), ("osm", 229), ("sd707", 230), ("dm-epri", 231), ("dm-tpri", 232), ("erpu-h", 233)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotType.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotType.setDescription('This variable indicates the type of the current slot')
hw8060SlotDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8060SlotDesc.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotDesc.setDescription('This variable indicates the description of the current slot; Max length is 64,0 indicates no description.')
hw8060SlotCpuRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotCpuRatio.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotCpuRatio.setDescription('This variable indicates the ratio of CPU the current slot occupied')
hw8060SlotPcbVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotPcbVersion.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotPcbVersion.setDescription('This variable indicates the PCB version of the current slot')
hw8060SlotSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotSoftwareVersion.setDescription('This variable indicates the software version of the current slot')
hw8060SlotSubslotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotSubslotNumber.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotSubslotNumber.setDescription('This variable indicates the total number of subslots in the current slot')
hw8060SlotAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotAdminStatus.setDescription('This variable indicates the administration status of the current slot')
hw8060SlotOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SlotOperStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060SlotOperStatus.setDescription('This variable indicates the operatrion status of the current slot')
hw8060SubslotTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3), )
if mibBuilder.loadTexts: hw8060SubslotTable.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotTable.setDescription('Subslot table.')
hw8060SubslotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060SlotIndex"), (0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hw8060SubslotEntry.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotEntry.setDescription('Subslot table entry.')
hw8060SubslotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SubslotIndex.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotIndex.setDescription('This variable indicates the index of the current subslot. Max value of index is 100,0 indicates none.')
hw8060SubslotType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SubslotType.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotType.setDescription('This variable indicates the type of the current subslot')
hw8060SubslotPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SubslotPortNum.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotPortNum.setDescription('This variable indicates the total number of ports in the current subslot')
hw8060SubslotAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SubslotAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060SubslotAdminStatus.setDescription('This variable indicates the administration status of the current subslot')
hw8060PortTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4), )
if mibBuilder.loadTexts: hw8060PortTable.setStatus('current')
if mibBuilder.loadTexts: hw8060PortTable.setDescription('Port table.')
hw8060PortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060SlotIndex"), (0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"), (0, "HUAWEI-AR46-DEV-ADM-MIB", "hw8060PortIndex"))
if mibBuilder.loadTexts: hw8060PortEntry.setStatus('current')
if mibBuilder.loadTexts: hw8060PortEntry.setDescription('Port table entry.')
hw8060PortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortIndex.setStatus('current')
if mibBuilder.loadTexts: hw8060PortIndex.setDescription('This variable indicates the index of the current port')
hw8060PortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortType.setStatus('current')
if mibBuilder.loadTexts: hw8060PortType.setDescription('This variable indicates the type of the current subslot')
hw8060PortDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortDesc.setStatus('current')
if mibBuilder.loadTexts: hw8060PortDesc.setDescription('This variable indicates the description of the current subslot')
hw8060PortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortSpeed.setStatus('current')
if mibBuilder.loadTexts: hw8060PortSpeed.setDescription('This variable indicates the speed in bps of the current subslot')
hw8060PortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060PortAdminStatus.setDescription('This variable indicates the administration status of the current subslot')
hw8060PortOperateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060PortOperateStatus.setStatus('current')
if mibBuilder.loadTexts: hw8060PortOperateStatus.setDescription('This variable indicates the operation status of the current subslot')
dev8060MPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 5), )
if mibBuilder.loadTexts: dev8060MPowerStatusTable.setStatus('current')
if mibBuilder.loadTexts: dev8060MPowerStatusTable.setDescription('the info about powers')
dev8060MPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 5, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "dev8060MPowerNum"))
if mibBuilder.loadTexts: dev8060MPowerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: dev8060MPowerStatusEntry.setDescription('the info about powers.')
dev8060MPowerNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dev8060MPowerNum.setStatus('current')
if mibBuilder.loadTexts: dev8060MPowerNum.setDescription('This variable indicates the sequence number of the current power. Max number is 10,0 indicates nonsupport this node.')
dev8060MPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dev8060MPowerStatus.setStatus('current')
if mibBuilder.loadTexts: dev8060MPowerStatus.setDescription('This variable indicates the working status of the current power. ok(1) the power state is normal. fail(2) the power state is abnormal. ')
dev8060MFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 6), )
if mibBuilder.loadTexts: dev8060MFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: dev8060MFanStatusTable.setDescription('the info about Fans')
dev8060MFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 6, 1), ).setIndexNames((0, "HUAWEI-AR46-DEV-ADM-MIB", "dev8060MFanNum"))
if mibBuilder.loadTexts: dev8060MFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: dev8060MFanStatusEntry.setDescription('the info about Fans.')
dev8060MFanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dev8060MFanNum.setStatus('current')
if mibBuilder.loadTexts: dev8060MFanNum.setDescription('This variable indicates the sequence number of the current fan. Max value is 10,0 indicates no fan.')
dev8060MFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ok", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dev8060MFanStatus.setStatus('current')
if mibBuilder.loadTexts: dev8060MFanStatus.setDescription('This variable indicates the working status of the current fan. ok(1) the fan state is normal. fail(2) the fan state is abnormal. ')
dev8060MGlobalTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7))
hw8060DevMRpuTemperature = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060DevMRpuTemperature.setStatus('current')
if mibBuilder.loadTexts: hw8060DevMRpuTemperature.setDescription('This variable indicates the temperature of RPU.')
hw8060DevMTemperatureMax = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8060DevMTemperatureMax.setStatus('current')
if mibBuilder.loadTexts: hw8060DevMTemperatureMax.setDescription('This variable indicates the maximum temperature set by user')
hw8060DevMTemperatureMin = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8060DevMTemperatureMin.setStatus('current')
if mibBuilder.loadTexts: hw8060DevMTemperatureMin.setDescription('This variable indicates the minimum temperature set by user')
hw8060SysVersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SysVersion.setStatus('current')
if mibBuilder.loadTexts: hw8060SysVersion.setDescription('This variable indicates the system version ( big version )')
hw8060SysTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060SysTime.setStatus('current')
if mibBuilder.loadTexts: hw8060SysTime.setDescription('This variable indicates the system time')
hw8060DevMVentTemperature = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 1, 7, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8060DevMVentTemperature.setStatus('current')
if mibBuilder.loadTexts: hw8060DevMVentTemperature.setDescription(' ')
hw8060DevNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2))
hwRpuTempTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 1))
if mibBuilder.loadTexts: hwRpuTempTooHigh.setStatus('current')
if mibBuilder.loadTexts: hwRpuTempTooHigh.setDescription('The notification indicates that the temperature of RPU is too high')
hwRpuTempOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 2))
if mibBuilder.loadTexts: hwRpuTempOK.setStatus('current')
if mibBuilder.loadTexts: hwRpuTempOK.setDescription('The notification indicates that The temperature of RPU is normal')
hwNpTempTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 3))
if mibBuilder.loadTexts: hwNpTempTooHigh.setStatus('current')
if mibBuilder.loadTexts: hwNpTempTooHigh.setDescription('The notification indicates that The temperature of NP exceeds the maximum')
hwNpTempOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 4))
if mibBuilder.loadTexts: hwNpTempOK.setStatus('current')
if mibBuilder.loadTexts: hwNpTempOK.setDescription('The notification indicates that The temperature of NP is normal')
hwRpuTempTooLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 5))
if mibBuilder.loadTexts: hwRpuTempTooLow.setStatus('current')
if mibBuilder.loadTexts: hwRpuTempTooLow.setDescription('The notification indicates that The temperature of RPU is too low')
hwNpTempTooLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 6))
if mibBuilder.loadTexts: hwNpTempTooLow.setStatus('current')
if mibBuilder.loadTexts: hwNpTempTooLow.setDescription('The notification indicates that The temperature of NP is too low')
hwVentTempTooHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 7))
if mibBuilder.loadTexts: hwVentTempTooHigh.setStatus('current')
if mibBuilder.loadTexts: hwVentTempTooHigh.setDescription('The notification indicates that The temperature of VENT exceeds the maximum')
hwVentTempOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 9))
if mibBuilder.loadTexts: hwVentTempOK.setStatus('current')
if mibBuilder.loadTexts: hwVentTempOK.setDescription('The notification indicates that The temperature of VENT is normal')
hwRpuReset = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 10))
if mibBuilder.loadTexts: hwRpuReset.setStatus('current')
if mibBuilder.loadTexts: hwRpuReset.setDescription('The notification indicates that the RPU reset')
hwRpuResetOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 11))
if mibBuilder.loadTexts: hwRpuResetOK.setStatus('current')
if mibBuilder.loadTexts: hwRpuResetOK.setDescription('The notification indicates that RPU reset successfully')
hwNpReset = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 12))
if mibBuilder.loadTexts: hwNpReset.setStatus('current')
if mibBuilder.loadTexts: hwNpReset.setDescription('The notification indicates that NP reset')
hwNpResetOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 13))
if mibBuilder.loadTexts: hwNpResetOK.setStatus('current')
if mibBuilder.loadTexts: hwNpResetOK.setDescription('The notification indicates that NP reset successfully')
hwSlotReset = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 14)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SlotIndex"))
if mibBuilder.loadTexts: hwSlotReset.setStatus('current')
if mibBuilder.loadTexts: hwSlotReset.setDescription('The notification indicates that Slot reset')
hwSlotResetOK = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 15)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SlotIndex"))
if mibBuilder.loadTexts: hwSlotResetOK.setStatus('current')
if mibBuilder.loadTexts: hwSlotResetOK.setDescription('The notification indicates that Slot reset successfully')
hwPciAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 16))
if mibBuilder.loadTexts: hwPciAlarm.setStatus('current')
if mibBuilder.loadTexts: hwPciAlarm.setDescription('The notification indicates that PCI alarm occurred')
hwPciNormal = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 17))
if mibBuilder.loadTexts: hwPciNormal.setStatus('current')
if mibBuilder.loadTexts: hwPciNormal.setDescription('The notification indicates that PCI is normal')
hwRpuIntReportErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 18))
if mibBuilder.loadTexts: hwRpuIntReportErr.setStatus('current')
if mibBuilder.loadTexts: hwRpuIntReportErr.setDescription('The notification indicates that RPU report wrong interrupts too frequently')
hwNpIntReportErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 19))
if mibBuilder.loadTexts: hwNpIntReportErr.setStatus('current')
if mibBuilder.loadTexts: hwNpIntReportErr.setDescription('The notification indicates that NP report wrong interrupts too frequently')
hwSlotIntReportErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 20)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwSlotIntReportErr.setStatus('current')
if mibBuilder.loadTexts: hwSlotIntReportErr.setDescription('The notification indicates that Slot report wrong interrupts too frequently')
hwWriteFlashErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 21))
if mibBuilder.loadTexts: hwWriteFlashErr.setStatus('current')
if mibBuilder.loadTexts: hwWriteFlashErr.setDescription('The notification indicates that Write FLASH failed')
hwPowerUnitFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 22)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "dev8060MPowerNum"))
if mibBuilder.loadTexts: hwPowerUnitFail.setStatus('current')
if mibBuilder.loadTexts: hwPowerUnitFail.setDescription('The notification indicates that Power failed')
hwPowerUnitNormal = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 23)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "dev8060MPowerNum"))
if mibBuilder.loadTexts: hwPowerUnitNormal.setStatus('current')
if mibBuilder.loadTexts: hwPowerUnitNormal.setDescription('The notification indicates that Power is normal')
hwFanUnitFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 24)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "dev8060MFanNum"))
if mibBuilder.loadTexts: hwFanUnitFail.setStatus('current')
if mibBuilder.loadTexts: hwFanUnitFail.setDescription('The notification indicates that Fan failed')
hwFanUnitNormal = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 25)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "dev8060MFanNum"))
if mibBuilder.loadTexts: hwFanUnitNormal.setStatus('current')
if mibBuilder.loadTexts: hwFanUnitNormal.setDescription('The notification indicates that Fan is normal')
hwFtpLoadFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 26))
if mibBuilder.loadTexts: hwFtpLoadFail.setStatus('current')
if mibBuilder.loadTexts: hwFtpLoadFail.setDescription('The notification indicates that FTP failed')
hwTftpLoadFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 27))
if mibBuilder.loadTexts: hwTftpLoadFail.setStatus('current')
if mibBuilder.loadTexts: hwTftpLoadFail.setDescription('The notification indicates that TFTP failed')
hwXmodemLoadFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 28))
if mibBuilder.loadTexts: hwXmodemLoadFail.setStatus('current')
if mibBuilder.loadTexts: hwXmodemLoadFail.setDescription('The notification indicates that XMODEM failed')
hwNpConfPathErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 29))
if mibBuilder.loadTexts: hwNpConfPathErr.setStatus('current')
if mibBuilder.loadTexts: hwNpConfPathErr.setDescription('The notification indicates that NP configuration path is abnormal')
hwHSCardConfPathErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 30)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwHSCardConfPathErr.setStatus('current')
if mibBuilder.loadTexts: hwHSCardConfPathErr.setDescription('The notification indicates that High speed card configuration path is abnormal')
hwLSCardJtagErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 31)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwLSCardJtagErr.setStatus('current')
if mibBuilder.loadTexts: hwLSCardJtagErr.setDescription('The notification indicates that Low speed card JTAG path is abnormal')
hwHSCardJtagErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 32)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwHSCardJtagErr.setStatus('current')
if mibBuilder.loadTexts: hwHSCardJtagErr.setDescription('The notification indicates that High speed card JTAG path is abnormal')
hwNpuJtagErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 33))
if mibBuilder.loadTexts: hwNpuJtagErr.setStatus('current')
if mibBuilder.loadTexts: hwNpuJtagErr.setDescription('The notification indicates that NP JTAG path is abnormal')
hwNpRpuDmuErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 34))
if mibBuilder.loadTexts: hwNpRpuDmuErr.setStatus('current')
if mibBuilder.loadTexts: hwNpRpuDmuErr.setDescription('The notification indicates that DMU path between NP and RPU is abnormal')
hwLSCardHealthyErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 35)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwLSCardHealthyErr.setStatus('current')
if mibBuilder.loadTexts: hwLSCardHealthyErr.setDescription('The notification indicates that Low speed card healthy signal is abnormal')
hwHSCardHealthyErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 36)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwHSCardHealthyErr.setStatus('current')
if mibBuilder.loadTexts: hwHSCardHealthyErr.setDescription('The notification indicates that High speed card healthy signal is abnormal')
hwCardPciHealthyErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 37)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwCardPciHealthyErr.setStatus('current')
if mibBuilder.loadTexts: hwCardPciHealthyErr.setDescription('The notification indicates that Slot PCI_HEALTHY signal is abnormal')
hwHSCardPowerErr = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 38)).setObjects(("HUAWEI-AR46-DEV-ADM-MIB", "hw8060SubslotIndex"))
if mibBuilder.loadTexts: hwHSCardPowerErr.setStatus('current')
if mibBuilder.loadTexts: hwHSCardPowerErr.setDescription('The notification indicates that Slot HEALTHY signal is invalid')
hwVentTempTooLow = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 2, 39))
if mibBuilder.loadTexts: hwVentTempTooLow.setStatus('current')
if mibBuilder.loadTexts: hwVentTempTooLow.setDescription('The notification indicates that the temperature of VENT is too low')
hw8060DevConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 33, 20, 3))
mibBuilder.exportSymbols("HUAWEI-AR46-DEV-ADM-MIB", hw8060SlotType=hw8060SlotType, hwRpuIntReportErr=hwRpuIntReportErr, dev8060MFanStatus=dev8060MFanStatus, hwNpIntReportErr=hwNpIntReportErr, hw8060PortOperateStatus=hw8060PortOperateStatus, hw8060SlotIndex=hw8060SlotIndex, hw8060SubslotTable=hw8060SubslotTable, hwNpTempOK=hwNpTempOK, dev8060MFanNum=dev8060MFanNum, hw8060PortTable=hw8060PortTable, hw8060DevObjects=hw8060DevObjects, hw8060PortType=hw8060PortType, hw8060FrameType=hw8060FrameType, hwNpuJtagErr=hwNpuJtagErr, hwFtpLoadFail=hwFtpLoadFail, hwVentTempOK=hwVentTempOK, hw8060SlotSoftwareVersion=hw8060SlotSoftwareVersion, hwNpReset=hwNpReset, hwPowerUnitFail=hwPowerUnitFail, hwRpuTempOK=hwRpuTempOK, dev8060MFanStatusEntry=dev8060MFanStatusEntry, hwRpuTempTooHigh=hwRpuTempTooHigh, hwPciNormal=hwPciNormal, hwSlotReset=hwSlotReset, hw8060DevNotifications=hw8060DevNotifications, hw8060SlotSubslotNumber=hw8060SlotSubslotNumber, dev8060MPowerStatusTable=dev8060MPowerStatusTable, hw8060SysVersion=hw8060SysVersion, dev8060MGlobalTable=dev8060MGlobalTable, hw8060SysTime=hw8060SysTime, hw8060DevMTemperatureMax=hw8060DevMTemperatureMax, hw8060PortEntry=hw8060PortEntry, hwSlotIntReportErr=hwSlotIntReportErr, hw8060SlotEntry=hw8060SlotEntry, hw8060SubslotIndex=hw8060SubslotIndex, hwLSCardHealthyErr=hwLSCardHealthyErr, hwRpuReset=hwRpuReset, hw8060SlotDesc=hw8060SlotDesc, hw8060DevMRpuTemperature=hw8060DevMRpuTemperature, hw8060PortDesc=hw8060PortDesc, hwWriteFlashErr=hwWriteFlashErr, hw8060SlotCpuRatio=hw8060SlotCpuRatio, PYSNMP_MODULE_ID=aR46_E200, hw8060SubslotPortNum=hw8060SubslotPortNum, hwSlotResetOK=hwSlotResetOK, hw8060SubslotEntry=hw8060SubslotEntry, hw8060PortIndex=hw8060PortIndex, hwNpConfPathErr=hwNpConfPathErr, hwNpTempTooHigh=hwNpTempTooHigh, hwVentTempTooLow=hwVentTempTooLow, hw8060FrameSlotNumber=hw8060FrameSlotNumber, hwNpResetOK=hwNpResetOK, hw8060SlotTable=hw8060SlotTable, hwHSCardPowerErr=hwHSCardPowerErr, hw8060SlotPcbVersion=hw8060SlotPcbVersion, hwRpuResetOK=hwRpuResetOK, dev8060MPowerStatusEntry=dev8060MPowerStatusEntry, hw8060DevConformance=hw8060DevConformance, aR46_E200=aR46_E200, hw8060DevMTemperatureMin=hw8060DevMTemperatureMin, dev8060MPowerStatus=dev8060MPowerStatus, hw8060SlotAdminStatus=hw8060SlotAdminStatus, hw8060FrameEntry=hw8060FrameEntry, hwCardPciHealthyErr=hwCardPciHealthyErr, hw8060PortAdminStatus=hw8060PortAdminStatus, hw8060FrameTable=hw8060FrameTable, dev8060MFanStatusTable=dev8060MFanStatusTable, hwNpRpuDmuErr=hwNpRpuDmuErr, hwVentTempTooHigh=hwVentTempTooHigh, hwHSCardHealthyErr=hwHSCardHealthyErr, hwHSCardJtagErr=hwHSCardJtagErr, hw8060FrameAdminStatus=hw8060FrameAdminStatus, hwPowerUnitNormal=hwPowerUnitNormal, hwPciAlarm=hwPciAlarm, hwXmodemLoadFail=hwXmodemLoadFail, hwLSCardJtagErr=hwLSCardJtagErr, hw8060PortSpeed=hw8060PortSpeed, hw8060FrameDesc=hw8060FrameDesc, hw8060SubslotAdminStatus=hw8060SubslotAdminStatus, hwRpuTempTooLow=hwRpuTempTooLow, hwNpTempTooLow=hwNpTempTooLow, hwFanUnitNormal=hwFanUnitNormal, hwHSCardConfPathErr=hwHSCardConfPathErr, hwTftpLoadFail=hwTftpLoadFail, hw8060FrameIndex=hw8060FrameIndex, hw8060DevMVentTemperature=hw8060DevMVentTemperature, hwFanUnitFail=hwFanUnitFail, dev8060MPowerNum=dev8060MPowerNum, hw8060SubslotType=hw8060SubslotType, hw8060SlotOperStatus=hw8060SlotOperStatus)
