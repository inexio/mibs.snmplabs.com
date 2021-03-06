#
# PySNMP MIB module SW-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, enterprises, iso, Counter64, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Bits, Integer32, NotificationType, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "enterprises", "iso", "Counter64", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Bits", "Integer32", "NotificationType", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2))
swL2DevMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1))
swL2DevCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1))
swL2DevCtrlStpState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlStpState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlStpState.setDescription('This object can be enabled or disabled spanning tree algorithm during runtime of the system.')
swL2DevCtrlPartitionModeState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlPartitionModeState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlPartitionModeState.setDescription('This object used to enable or disable port auto partition. When the object apply for all ports of the device.')
swL2DevCtrlTableLockState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlTableLockState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlTableLockState.setDescription("This object indicates whether the address table is locked. In other words, the address table doesn't learn any more new address. The aging timer is suspended when the address table is locked. As long as the table is locked, all of the frames are dropped if the destination can not be found in the address.")
swL2DevCtrlHOLState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlHOLState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlHOLState.setDescription("The object provides a way to prevent HOL (Head Of Line) blocking between ports. HOL protection may prevent forwarding a packet to a blocking port. The idea relies on the assumption that it is better to discard packets destined to blocking ports, then to let them consume more and more buffers in the input-port's Rx-counters because eventually these input ports may become totally blocked. The meanings of the values are: other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. disabled(2) - HOL function disable for device. enabled(3) - HOL function enable for device.")
swL2DevCtrlAddrLookupModesAndHitRate = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("level0", 1), ("level1", 2), ("level2", 3), ("level3", 4), ("level4", 5), ("level5", 6), ("level6", 7), ("level7", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlAddrLookupModesAndHitRate.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlAddrLookupModesAndHitRate.setDescription('According to the differnet address looke mode setting, to enlarge the address table size is possible in device. But there is side effect as the higher level you have, the lower thorughput device has. That means Level 0 get the smallest table size, but get better performace. We recommand the user use the Level 1 as defualt setting.')
swL2DevCtrlBuzzerState = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevCtrlBuzzerState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlBuzzerState.setDescription(' Controls buzzer state to be disabled or enabled.')
swL2DevCtrlBuzzerTest = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 1, 7), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swL2DevCtrlBuzzerTest.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevCtrlBuzzerTest.setDescription(' Tests buzzer to bibi. First of all, any unsigned integer can be used to set.')
swL2DevAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2))
swL2DevAlarmPartition = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmPartition.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPartition.setDescription("Depending on this object, the device send a trap or not when any one of the device's ports was partitioned.")
swL2DevAlarmNewRoot = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmNewRoot.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmNewRoot.setDescription('When the device has become the new root of the Spanning Tree, this object decide whether to send a new root trap.')
swL2DevAlarmTopChange = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmTopChange.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmTopChange.setDescription("This object determines to send a trap or not when the switch topology was changed. If the object is enabled(3), the topologyChange trap is sent by the device when any of its configured ports transitions from the Learning state to the Forwarding state, or from the Forwarding state to the Blocking state. For the same port tranition, the device doesn't send the trap if this object value is disabled or other.")
swL2DevAlarmLinkChange = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmLinkChange.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmLinkChange.setDescription("This object determines to send a trap or not when the link was changed. If the object is enabled(3), the Link Change trap is sent by the device when any of its ports link change. The device doesn't send the trap if this object value is disabled or other.")
swL2DevAlarmPowerTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5), )
if mibBuilder.loadTexts: swL2DevAlarmPowerTable.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerTable.setDescription('A table that controls error state to bibi about power module.')
swL2DevAlarmPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1), ).setIndexNames((0, "SW-COMMON-MIB", "swL2DevAlarmPowerIndex"))
if mibBuilder.loadTexts: swL2DevAlarmPowerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerEntry.setDescription('A list of controlling informations for power module.')
swL2DevAlarmPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2DevAlarmPowerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerIndex.setDescription('ID of the power module.')
swL2DevAlarmPowerTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmPowerTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerTemperature.setDescription('Controls temperature error state in power module.')
swL2DevAlarmPowerVolt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmPowerVolt.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerVolt.setDescription('Controls volt error state in power module.')
swL2DevAlarmPowerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmPowerCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerCurrent.setDescription('Controls current error state in power module.')
swL2DevAlarmPowerFan = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmPowerFan.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmPowerFan.setDescription('Controls fan error state in power module.')
swL2DevAlarmSystemFanTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6), )
if mibBuilder.loadTexts: swL2DevAlarmSystemFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmSystemFanTable.setDescription('A table that controls error state to bibi about system fans.')
swL2DevAlarmSystemFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1), ).setIndexNames((0, "SW-COMMON-MIB", "swL2DevAlarmSystemFanIndex"))
if mibBuilder.loadTexts: swL2DevAlarmSystemFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmSystemFanEntry.setDescription('A list of controlling informations for system fans.')
swL2DevAlarmSystemFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2DevAlarmSystemFanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmSystemFanIndex.setDescription('ID of the system fans.')
swL2DevAlarmSystemFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 1, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2DevAlarmSystemFanState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2DevAlarmSystemFanState.setDescription('Controls system fan error state.')
mibBuilder.exportSymbols("SW-COMMON-MIB", swL2DevCtrlStpState=swL2DevCtrlStpState, swL2DevAlarmSystemFanState=swL2DevAlarmSystemFanState, swL2DevAlarmLinkChange=swL2DevAlarmLinkChange, systems=systems, swL2DevCtrlBuzzerState=swL2DevCtrlBuzzerState, swL2DevAlarmPowerFan=swL2DevAlarmPowerFan, swL2DevAlarmPowerIndex=swL2DevAlarmPowerIndex, swL2DevCtrlAddrLookupModesAndHitRate=swL2DevCtrlAddrLookupModesAndHitRate, external=external, swL2DevCtrl=swL2DevCtrl, swL2DevCtrlPartitionModeState=swL2DevCtrlPartitionModeState, dlinkcommon=dlinkcommon, swL2DevAlarm=swL2DevAlarm, swL2DevCtrlBuzzerTest=swL2DevCtrlBuzzerTest, swL2DevAlarmPowerTable=swL2DevAlarmPowerTable, swL2DevAlarmPowerVolt=swL2DevAlarmPowerVolt, swL2Mgmt=swL2Mgmt, dlink=dlink, es2000Mgmt=es2000Mgmt, marconi_mgmt=marconi_mgmt, swL2DevAlarmPowerEntry=swL2DevAlarmPowerEntry, swL2DevMgmt=swL2DevMgmt, golf=golf, swL2DevAlarmPowerCurrent=swL2DevAlarmPowerCurrent, golfproducts=golfproducts, swL2DevAlarmTopChange=swL2DevAlarmTopChange, swL2DevAlarmSystemFanIndex=swL2DevAlarmSystemFanIndex, swL2DevAlarmPartition=swL2DevAlarmPartition, golfcommon=golfcommon, swL2DevAlarmPowerTemperature=swL2DevAlarmPowerTemperature, marconi=marconi, swL2DevCtrlTableLockState=swL2DevCtrlTableLockState, swL2DevAlarmNewRoot=swL2DevAlarmNewRoot, swL2DevAlarmSystemFanEntry=swL2DevAlarmSystemFanEntry, es2000=es2000, swL2DevCtrlHOLState=swL2DevCtrlHOLState, swL2DevAlarmSystemFanTable=swL2DevAlarmSystemFanTable)
