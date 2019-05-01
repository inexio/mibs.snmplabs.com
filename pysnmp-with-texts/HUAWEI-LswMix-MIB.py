#
# PySNMP MIB module HUAWEI-LswMix-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswMix-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
hwLswFrameIndex, hwLswSlotIndex = mibBuilder.importSymbols("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex", "hwLswSlotIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, MibIdentifier, Bits, Counter32, Counter64, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "MibIdentifier", "Bits", "Counter32", "Counter64", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwLswMix = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17))
hwLswMix.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLswMix.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwLswMix.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswMix.setOrganization('')
if mibBuilder.loadTexts: hwLswMix.setContactInfo('')
if mibBuilder.loadTexts: hwLswMix.setDescription('')
hwLswLastSwitchDate = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswLastSwitchDate.setStatus('current')
if mibBuilder.loadTexts: hwLswLastSwitchDate.setDescription('This object indicates the date of the most recent change to the mpu(Main Processing Unit). ')
hwLswLastSwitchTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswLastSwitchTime.setStatus('current')
if mibBuilder.loadTexts: hwLswLastSwitchTime.setDescription('This object indicates the time of the most recent change to the mpu. ')
hwLswMpuSwitchsNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswMpuSwitchsNum.setStatus('current')
if mibBuilder.loadTexts: hwLswMpuSwitchsNum.setDescription('This object indicates the total times of the mpu switched since the system start up. ')
hwLswMpuSwitch = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("switch", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswMpuSwitch.setStatus('current')
if mibBuilder.loadTexts: hwLswMpuSwitch.setDescription('Setting this object will immediately switch the standby mpu to master mpu. Read is not supported. ')
hwLswXSlotTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5), )
if mibBuilder.loadTexts: hwLswXSlotTable.setStatus('current')
if mibBuilder.loadTexts: hwLswXSlotTable.setDescription('The source main table.')
hwLswXSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1), ).setIndexNames((0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"), (0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
if mibBuilder.loadTexts: hwLswXSlotEntry.setStatus('current')
if mibBuilder.loadTexts: hwLswXSlotEntry.setDescription('An entry in the source main table.')
hwLswMainCardBoardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("standby", 2), ("process", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswMainCardBoardStatus.setStatus('current')
if mibBuilder.loadTexts: hwLswMainCardBoardStatus.setDescription('The value describes whether the board is master, standby or process. master and standby are the possible states for the mpu, while process indicates the state of lpu(Line Processing Unit)')
hwLswCrossBarStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("master", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswCrossBarStatus.setStatus('current')
if mibBuilder.loadTexts: hwLswCrossBarStatus.setDescription("The value describes whether the crossbar is master or standby. It is master when it's in the master mpu board, standby when in the standby mpu. But both crossbars in mpus are master when the device in load-balance mode.")
hwsMixTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 10))
hwSlaveSwitchOver = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 10, 1))
if mibBuilder.loadTexts: hwSlaveSwitchOver.setStatus('current')
if mibBuilder.loadTexts: hwSlaveSwitchOver.setDescription('An hwSlaveSwitchOver trap signifies that the action of standby mpu switching to master has completed. ')
mibBuilder.exportSymbols("HUAWEI-LswMix-MIB", hwLswLastSwitchTime=hwLswLastSwitchTime, hwLswXSlotEntry=hwLswXSlotEntry, hwLswMainCardBoardStatus=hwLswMainCardBoardStatus, hwLswLastSwitchDate=hwLswLastSwitchDate, hwLswMpuSwitchsNum=hwLswMpuSwitchsNum, hwLswXSlotTable=hwLswXSlotTable, hwLswCrossBarStatus=hwLswCrossBarStatus, hwsMixTrapMib=hwsMixTrapMib, PYSNMP_MODULE_ID=hwLswMix, hwLswMpuSwitch=hwLswMpuSwitch, hwSlaveSwitchOver=hwSlaveSwitchOver, hwLswMix=hwLswMix)
