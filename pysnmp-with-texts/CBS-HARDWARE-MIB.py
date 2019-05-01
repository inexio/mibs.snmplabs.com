#
# PySNMP MIB module CBS-HARDWARE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CBS-HARDWARE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cbsMIBs, cbsTraps, cbsMgmt = mibBuilder.importSymbols("CROSSBEAM-SYSTEMS-MIB", "cbsMIBs", "cbsTraps", "cbsMgmt")
ProductID, KBytes = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "ProductID", "KBytes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, Gauge32, Counter32, ModuleIdentity, ObjectIdentity, iso, Bits, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cbsHardwareMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6848, 3, 2))
cbsHardwareMIB.setRevisions(('2002-03-15 00:00', '2002-08-21 00:00', '2003-05-08 00:00', '2003-07-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cbsHardwareMIB.setRevisionsDescriptions(('Initial Revision', 'Added bootwait state to hardware module status.', 'Added separate objects for AC & DC power supply/feed.', 'Added Trap definitions for DBHA link up/down.',))
if mibBuilder.loadTexts: cbsHardwareMIB.setLastUpdated('200305080000Z')
if mibBuilder.loadTexts: cbsHardwareMIB.setOrganization('Crossbeam Systems, Inc.')
if mibBuilder.loadTexts: cbsHardwareMIB.setContactInfo('Email: mib-admin@crossbeamsys.com Postal: 200 Baker Avenue Concord MA 01742')
if mibBuilder.loadTexts: cbsHardwareMIB.setDescription('This MIB module defines the objects to identify and monitor Crossbeam Systems hardware.')
class OperationalState(TextualConvention, Integer32):
    description = 'The operational state of a hardware subsystem.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("not-present", 3))

class ExistentialState(TextualConvention, Integer32):
    description = 'Indicates the component exists.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("present", 1), ("not-present", 2))

cbsHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2, 1))
cbsHwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 4, 1))
cbsHwSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2, 1, 1))
cbsHwSystemStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2))
cbsHwSystemProductID = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 1), ProductID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemProductID.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemProductID.setDescription('The identifier for this system')
cbsHwSystemDescription = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemDescription.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemDescription.setDescription('A textual description of the product.')
cbsHwSystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemSerialNumber.setDescription('The serial number of the system.')
cbsHwSystemBackplaneRevision = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemBackplaneRevision.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemBackplaneRevision.setDescription('The Revision of the system backplane.')
cbsHwSystemRedundentPowerSupplyStatus = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 1), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemRedundentPowerSupplyStatus.setStatus('obsolete')
if mibBuilder.loadTexts: cbsHwSystemRedundentPowerSupplyStatus.setDescription('Indicates that the redundent power supply is operational. This object is obsoleted in favor of separate objects for AC and DC power supply.')
cbsHwSystemRedundentPowerFeedStatus = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 2), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemRedundentPowerFeedStatus.setStatus('obsolete')
if mibBuilder.loadTexts: cbsHwSystemRedundentPowerFeedStatus.setDescription('Indicates that both of the redundent backplane power feeds are operational. This object is obsoleted in favor of separate objects for AC and DC power feed.')
cbsHwSystemChassisTemp = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemChassisTemp.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemChassisTemp.setDescription('The temperature of the chassis air flow as measured at the upper fan tray.')
cbsHwSystemUpperFanTray = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 4), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemUpperFanTray.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemUpperFanTray.setDescription('The upper fan tray is present in the system.')
cbsHwSystemLowerFanTray = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 5), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemLowerFanTray.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemLowerFanTray.setDescription('The lower fan tray is present in the system.')
cbsHwSystemAlarm = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("minor", 2), ("major", 3), ("critical", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemAlarm.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemAlarm.setDescription('Indicates the highest current alarm state of the system.')
cbsHwSystemPowerType = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ac", 1), ("dc", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemPowerType.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemPowerType.setDescription('Indicates the power type of the system.')
cbsHwSystemRedundentACPowerSupplyStatus = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 8), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemRedundentACPowerSupplyStatus.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemRedundentACPowerSupplyStatus.setDescription('Indicates that the redundent AC power supply is operational. Will return down (i.e. not-operational) for DC chassis.')
cbsHwSystemRedundentACPowerFeedStatus = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 9), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemRedundentACPowerFeedStatus.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemRedundentACPowerFeedStatus.setDescription('Indicates that both of the redundent backplane AC power feeds are operational. Will return down (i.e. not-operational) for DC chassis.')
cbsHwSystemDCPowerFilterA = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 10), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemDCPowerFilterA.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemDCPowerFilterA.setDescription('Indicates if DC power filter A is present or not present. Will return not present for AC chassis.')
cbsHwSystemDCPowerFilterB = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 11), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemDCPowerFilterB.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemDCPowerFilterB.setDescription('Indicates if DC power filter B is present or not present. Will return not present for AC chassis.')
cbsHwSystemDCPowerFeedA = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 12), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemDCPowerFeedA.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemDCPowerFeedA.setDescription('Indicates if DC power feed A is present or not present. Will return not present for AC chassis.')
cbsHwSystemDCPowerFeedB = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 2, 13), ExistentialState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSystemDCPowerFeedB.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemDCPowerFeedB.setDescription('Indicates if DC power feed B is present or not present. Will return not present for AC chassis.')
cbsFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 1, 3), )
if mibBuilder.loadTexts: cbsFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: cbsFanStatusTable.setDescription('This table contains information about the fan trays currently installed in the system.')
cbsFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1), ).setIndexNames((0, "CBS-HARDWARE-MIB", "cbsFanGroupIndex"), (0, "CBS-HARDWARE-MIB", "cbsFanIndex"))
if mibBuilder.loadTexts: cbsFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cbsFanStatusEntry.setDescription('An entry in the hardware module table.')
cbsFanGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2))))
if mibBuilder.loadTexts: cbsFanGroupIndex.setStatus('current')
if mibBuilder.loadTexts: cbsFanGroupIndex.setDescription('Index of the fan tray.')
cbsFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9)))
if mibBuilder.loadTexts: cbsFanIndex.setStatus('current')
if mibBuilder.loadTexts: cbsFanIndex.setDescription('The fan number in the fan tray.')
cbsFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 3, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsFanStatus.setStatus('current')
if mibBuilder.loadTexts: cbsFanStatus.setDescription('Operational status of the fan.')
cbsHwModuleTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4), )
if mibBuilder.loadTexts: cbsHwModuleTable.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleTable.setDescription('This table contains information about the processor modules currently installed in the system.')
cbsHwModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1), ).setIndexNames((0, "CBS-HARDWARE-MIB", "cbsHwModuleID"))
if mibBuilder.loadTexts: cbsHwModuleEntry.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleEntry.setDescription('An entry in the hardware module table.')
cbsHwModuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleID.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleID.setDescription('The product ID for the module.')
cbsHwModuleProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 2), ProductID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleProductID.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleProductID.setDescription('The product ID for the module.')
cbsHwModuleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDescription.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDescription.setDescription('A short description of the module.')
cbsHwModuleBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleBoardRevision.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleBoardRevision.setDescription('The board revision level of the module.')
cbsHwModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleSerialNumber.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleSerialNumber.setDescription('The serial number of the module.')
cbsHwModuleBootStrapRev = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleBootStrapRev.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleBootStrapRev.setDescription('Total static DRAM memory on the module in Kilobytes.')
cbsHwModuleBootloaderRev = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleBootloaderRev.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleBootloaderRev.setDescription('Total static DRAM memory on the module in Kilobytes.')
cbsHwModuleDiagnosticsRev = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDiagnosticsRev.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDiagnosticsRev.setDescription('Total static DRAM memory on the module in Kilobytes.')
cbsHwModuleSDRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 9), KBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleSDRAMSize.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleSDRAMSize.setDescription('Total Static DRAM memory on the module in Kilobytes.')
cbsHwModuleRDRAMSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 10), KBytes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleRDRAMSize.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleRDRAMSize.setDescription('Total RDRAM memory on the module in Kilobytes.')
cbsHwModuleDiskAPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDiskAPresent.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDiskAPresent.setDescription('The first disk storage device is present.')
cbsHwModuleDiskBPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDiskBPresent.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDiskBPresent.setDescription('The second disk storage device is present.')
cbsHwModuleDuartAPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDuartAPresent.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDuartAPresent.setDescription('The first DUART device is present on the module.')
cbsHwModuleDuartBPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleDuartBPresent.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleDuartBPresent.setDescription('The second DUART device is present on the module.')
cbsHwModuleAccelCard1Present = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleAccelCard1Present.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleAccelCard1Present.setDescription('The Accelerator Card 1 is present on the module.')
cbsHwModuleAccelCard2Present = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 4, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleAccelCard2Present.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleAccelCard2Present.setDescription('The Accelerator Card 2 is present on the module.')
cbsHwComponentRevTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 1, 5), )
if mibBuilder.loadTexts: cbsHwComponentRevTable.setStatus('current')
if mibBuilder.loadTexts: cbsHwComponentRevTable.setDescription('A table containing the revision level of programable hardware components.')
cbsHwComponentRevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1), ).setIndexNames((0, "CBS-HARDWARE-MIB", "cbsHwModuleID"), (0, "CBS-HARDWARE-MIB", "cbsHwComponentIndex"))
if mibBuilder.loadTexts: cbsHwComponentRevEntry.setStatus('current')
if mibBuilder.loadTexts: cbsHwComponentRevEntry.setDescription('An entry in the hardware component revision table.')
cbsHwComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cbsHwComponentIndex.setStatus('current')
if mibBuilder.loadTexts: cbsHwComponentIndex.setDescription('Description of the programable component')
cbsHwComponentDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwComponentDescription.setStatus('current')
if mibBuilder.loadTexts: cbsHwComponentDescription.setDescription('Description of the programable component')
cbsHwComponentRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwComponentRevision.setStatus('current')
if mibBuilder.loadTexts: cbsHwComponentRevision.setDescription('Revision level of the programable component')
cbsHwModuleStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6), )
if mibBuilder.loadTexts: cbsHwModuleStatusTable.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleStatusTable.setDescription('This table contains the status of processor modules currently installed in the system.')
cbsHwModuleStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1), )
cbsHwModuleEntry.registerAugmentions(("CBS-HARDWARE-MIB", "cbsHwModuleStatusEntry"))
cbsHwModuleStatusEntry.setIndexNames(*cbsHwModuleEntry.getIndexNames())
if mibBuilder.loadTexts: cbsHwModuleStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleStatusEntry.setDescription('An entry in the hardware module status table.')
cbsHwModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unavailable", 1), ("down", 2), ("initializing", 3), ("up", 4), ("standby", 5), ("bootwait", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleStatus.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleStatus.setDescription('The operational state of the module unavailable - No status is currently available for this module. down - The module is currently down. initializing - The module is loading. up - The module is in an operational state. standby - The module is operating in standby mode. bootwait - The module is waiting for resources to become available so it can load software.')
cbsHwModuleCpuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleCpuTemp.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleCpuTemp.setDescription('The current CPU temperature in degrees centigrade.')
cbsHwModuleFPGATemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 75))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleFPGATemp.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleFPGATemp.setDescription('The current FPGA temperature in degrees centigrade.')
cbsHwModuleInTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 75))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleInTemp.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleInTemp.setDescription('The current temperature at the sensor located at the bottom of the board in degrees centigrade.')
cbsHwModuleInTempAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleInTempAlarm.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleInTempAlarm.setDescription('Indicates a high temperature alarm for the bottom board sensor.')
cbsHwModuleExhaustTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 75))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleExhaustTemp.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleExhaustTemp.setDescription('The current temperature at the sensor located at the top of the board in degrees centigrade.')
cbsHwModuleExhaustTempAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleExhaustTempAlarm.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleExhaustTempAlarm.setDescription('Indicates a high temperature alarm for the top board sensor.')
cbsHwModuleCPUVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleCPUVoltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleCPUVoltage.setDescription('The current voltage level of the processor supply. This number is in 1/100ths of a volt and the ideal value depends on the speed of the processor.')
cbsHwModule1_8Voltage = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 9), Gauge32()).setLabel("cbsHwModule1-8Voltage").setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModule1_8Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModule1_8Voltage.setDescription('The current voltage level of the 1.8 volt power supply. This number is in 1/100ths of a volt and the ideal value of 1.8 volts will be read as 180.')
cbsHwModule3_3Voltage = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 10), Gauge32()).setLabel("cbsHwModule3-3Voltage").setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModule3_3Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModule3_3Voltage.setDescription('The current voltage level of the 3.3 volt power supply. This number is in 1/100ths of a volt and the ideal value of 3.3 volts will be read as 330.')
cbsHwModule2_5Voltage = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 11), Gauge32()).setLabel("cbsHwModule2-5Voltage").setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModule2_5Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModule2_5Voltage.setDescription('The current voltage level of the 2.5 volt power supply. This number is in 1/100ths of a volt and the ideal value of 2.5 volts will be read as 250.')
cbsHwModuleControlLinkA = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 12), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleControlLinkA.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleControlLinkA.setDescription('The operation state of control link A.')
cbsHwModuleControlLinkB = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 13), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleControlLinkB.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleControlLinkB.setDescription('The Operational state of control link B.')
cbsHwModuleActiveLED = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleActiveLED.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleActiveLED.setDescription("Indicates the board's active LED is on.")
cbsHwModuleStandbyLED = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleStandbyLED.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleStandbyLED.setDescription("Indicates the board's standby LED is on.")
cbsHwModuleFailedLED = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleFailedLED.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleFailedLED.setDescription("Indicates the board's failed LED is on.")
cbsHwModuleCpu2Temp = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-25, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleCpu2Temp.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleCpu2Temp.setDescription("For dual processor modules, 2nd CPU's current temperature in degrees centigrade. For modules that don't support it, a special invalid value of 10000 will be returned.")
cbsHwModuleCPU2Voltage = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 18), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleCPU2Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleCPU2Voltage.setDescription("For dual processor modules, 2nd CPU's current voltage level. This number is in 1/100ths of a volt and the ideal value depends on the speed of the processor. For modules that don't support it, a special invalid value of 10000 will be returned.")
cbsHwModuleFPGA1_8Voltage = MibScalar((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 19), Gauge32()).setLabel("cbsHwModuleFPGA1-8Voltage").setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModuleFPGA1_8Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleFPGA1_8Voltage.setDescription("FPGA's current voltage level of the 1.8 volt power supply. This number is in 1/100ths of a volt and the ideal value of 1.8 volts will be read as 180. For modules that don't support it, a special invalid value of 10000 will be returned.")
cbsHwModule125Voltage = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 6, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwModule125Voltage.setStatus('current')
if mibBuilder.loadTexts: cbsHwModule125Voltage.setDescription("Current voltage level of the 1.25 volt power supply. This number is in 1/100ths of a volt and the ideal value of 1.25 volts will be read as 125. For modules that don't support it, a special invalid value of 10000 will be returned.")
cbsHwSdpStatusTable = MibTable((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7), )
if mibBuilder.loadTexts: cbsHwSdpStatusTable.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpStatusTable.setDescription('Table containing status of the Switched Data Path backplane links.')
cbsHwSdpStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1), ).setIndexNames((0, "CBS-HARDWARE-MIB", "cbsHwSdpNpmSlot"), (0, "CBS-HARDWARE-MIB", "cbsHwSdpRemoteSlot"))
if mibBuilder.loadTexts: cbsHwSdpStatusEntry.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpStatusEntry.setDescription('An entry in the hardware SDP status table.')
cbsHwSdpNpmSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: cbsHwSdpNpmSlot.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpNpmSlot.setDescription('The slot number of the Network Processor Module end of the link')
cbsHwSdpRemoteSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 14)))
if mibBuilder.loadTexts: cbsHwSdpRemoteSlot.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpRemoteSlot.setDescription('The slot number of the remote end of the link')
cbsHwSdpNpmState = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSdpNpmState.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpNpmState.setDescription('The operational state of the NPM side of the link.')
cbsHwSdpRemoteState = MibTableColumn((1, 3, 6, 1, 4, 1, 6848, 2, 1, 7, 1, 4), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbsHwSdpRemoteState.setStatus('current')
if mibBuilder.loadTexts: cbsHwSdpRemoteState.setDescription('The operational state of the remote end of the link.')
cbsHwPowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 1))
if mibBuilder.loadTexts: cbsHwPowerSupplyFailed.setStatus('current')
if mibBuilder.loadTexts: cbsHwPowerSupplyFailed.setDescription('One of the redundent power supplies or DC filters has failed or been removed.')
cbsHwPowerSupplyRecovered = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 2))
if mibBuilder.loadTexts: cbsHwPowerSupplyRecovered.setStatus('current')
if mibBuilder.loadTexts: cbsHwPowerSupplyRecovered.setDescription('A redundent power supply or DC filter that was previously failed or missing has been replaced.')
cbsHwPowerFeedFailed = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 3))
if mibBuilder.loadTexts: cbsHwPowerFeedFailed.setStatus('current')
if mibBuilder.loadTexts: cbsHwPowerFeedFailed.setDescription('One of the redundent backplane power feed has failed.')
cbsHwPowerFeedRecovered = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 4))
if mibBuilder.loadTexts: cbsHwPowerFeedRecovered.setStatus('current')
if mibBuilder.loadTexts: cbsHwPowerFeedRecovered.setDescription('One of the redundent backplane power feed that previously not working has become operational.')
cbsHwUpperFanTrayInserted = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 5))
if mibBuilder.loadTexts: cbsHwUpperFanTrayInserted.setStatus('current')
if mibBuilder.loadTexts: cbsHwUpperFanTrayInserted.setDescription('A fan tray has been inserted into the system.')
cbsHwUpperFanTrayRemoved = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 6))
if mibBuilder.loadTexts: cbsHwUpperFanTrayRemoved.setStatus('current')
if mibBuilder.loadTexts: cbsHwUpperFanTrayRemoved.setDescription('A fan tray has been removed from the system.')
cbsHwLowerFanTrayInserted = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 7))
if mibBuilder.loadTexts: cbsHwLowerFanTrayInserted.setStatus('current')
if mibBuilder.loadTexts: cbsHwLowerFanTrayInserted.setDescription('A fan tray has been inserted into the system.')
cbsHwLowerFanTrayRemoved = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 8))
if mibBuilder.loadTexts: cbsHwLowerFanTrayRemoved.setStatus('current')
if mibBuilder.loadTexts: cbsHwLowerFanTrayRemoved.setDescription('A fan tray has been removed from the system.')
cbsHwFanFailed = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 9)).setObjects(("CBS-HARDWARE-MIB", "cbsFanStatus"))
if mibBuilder.loadTexts: cbsHwFanFailed.setStatus('current')
if mibBuilder.loadTexts: cbsHwFanFailed.setDescription('One of the system cooling fans has failed.')
cbsHwFanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 10)).setObjects(("CBS-HARDWARE-MIB", "cbsFanStatus"))
if mibBuilder.loadTexts: cbsHwFanRecovered.setStatus('current')
if mibBuilder.loadTexts: cbsHwFanRecovered.setDescription('A Fan that was inoperative has recovered.')
cbsHwSystemAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 11)).setObjects(("CBS-HARDWARE-MIB", "cbsHwSystemAlarm"))
if mibBuilder.loadTexts: cbsHwSystemAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: cbsHwSystemAlarmTrap.setDescription('Indicates that the alarm state of the system has changed.')
cbsHwChassisTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 12)).setObjects(("CBS-HARDWARE-MIB", "cbsHwSystemChassisTemp"))
if mibBuilder.loadTexts: cbsHwChassisTempExceeded.setStatus('current')
if mibBuilder.loadTexts: cbsHwChassisTempExceeded.setDescription('Indicates the the chassis temperature, as measure at the exhaust fan has exceeded the maximum.')
cbsHwChassisTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 13)).setObjects(("CBS-HARDWARE-MIB", "cbsHwSystemChassisTemp"))
if mibBuilder.loadTexts: cbsHwChassisTempNormal.setStatus('current')
if mibBuilder.loadTexts: cbsHwChassisTempNormal.setDescription('Indicates the the chassis temperature, as measure at the exhaust fan has returned to normal.')
cbsHwModuleStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 14)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleStatus"))
if mibBuilder.loadTexts: cbsHwModuleStatusChanged.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleStatusChanged.setDescription('The status of a processor module has changed, the new status of the module that has changed is reported.')
cbsHwModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 15)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleID"))
if mibBuilder.loadTexts: cbsHwModuleInserted.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleInserted.setDescription('A processor module been inserted into the system, reports the slot number of the module that has been inserted.')
cbsHwModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 16)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleID"))
if mibBuilder.loadTexts: cbsHwModuleRemoved.setStatus('current')
if mibBuilder.loadTexts: cbsHwModuleRemoved.setDescription('A processor module been removed into the system, reports the slot number of the module that has been removed.')
cbsModuleTempExceeded = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 17)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleCpuTemp"))
if mibBuilder.loadTexts: cbsModuleTempExceeded.setStatus('current')
if mibBuilder.loadTexts: cbsModuleTempExceeded.setDescription('Indicates that the module CPU temperature has execeeded the high limit.')
cbsModuleTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 18)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleCpuTemp"))
if mibBuilder.loadTexts: cbsModuleTempNormal.setStatus('current')
if mibBuilder.loadTexts: cbsModuleTempNormal.setDescription('Indicates that the module CPU temperature has returned to the normal operating range.')
cbsDbhaLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 19)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleID"))
if mibBuilder.loadTexts: cbsDbhaLinkUp.setStatus('current')
if mibBuilder.loadTexts: cbsDbhaLinkUp.setDescription('The DBHA link on this CPM has come up.')
cbsDbhaLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 6848, 4, 1, 20)).setObjects(("CBS-HARDWARE-MIB", "cbsHwModuleID"))
if mibBuilder.loadTexts: cbsDbhaLinkDown.setStatus('current')
if mibBuilder.loadTexts: cbsDbhaLinkDown.setDescription('The DBHA link on this CPM has failed.')
mibBuilder.exportSymbols("CBS-HARDWARE-MIB", ExistentialState=ExistentialState, cbsHwSystemDescription=cbsHwSystemDescription, cbsHwChassisTempNormal=cbsHwChassisTempNormal, cbsHwComponentRevTable=cbsHwComponentRevTable, cbsHwModuleSDRAMSize=cbsHwModuleSDRAMSize, cbsHwChassisTempExceeded=cbsHwChassisTempExceeded, cbsHwSystemSerialNumber=cbsHwSystemSerialNumber, cbsHwSystemAlarm=cbsHwSystemAlarm, cbsHwModuleInTemp=cbsHwModuleInTemp, cbsHwModuleID=cbsHwModuleID, cbsHwTraps=cbsHwTraps, cbsHwModuleCPU2Voltage=cbsHwModuleCPU2Voltage, cbsHwSystemAlarmTrap=cbsHwSystemAlarmTrap, cbsModuleTempExceeded=cbsModuleTempExceeded, cbsHwModuleTable=cbsHwModuleTable, cbsHwModuleActiveLED=cbsHwModuleActiveLED, cbsHwSystemProductID=cbsHwSystemProductID, cbsHwModuleStatusChanged=cbsHwModuleStatusChanged, cbsHwSystemDCPowerFilterB=cbsHwSystemDCPowerFilterB, cbsHwComponentDescription=cbsHwComponentDescription, cbsHwModuleInserted=cbsHwModuleInserted, cbsHwModuleFPGATemp=cbsHwModuleFPGATemp, cbsFanIndex=cbsFanIndex, cbsHwModuleStandbyLED=cbsHwModuleStandbyLED, cbsHwModuleRemoved=cbsHwModuleRemoved, cbsHwModule125Voltage=cbsHwModule125Voltage, cbsHwSystemRedundentACPowerSupplyStatus=cbsHwSystemRedundentACPowerSupplyStatus, cbsHwModuleCPUVoltage=cbsHwModuleCPUVoltage, cbsHwComponentRevEntry=cbsHwComponentRevEntry, cbsHwModuleFailedLED=cbsHwModuleFailedLED, cbsHwModuleStatusTable=cbsHwModuleStatusTable, cbsFanStatusTable=cbsFanStatusTable, cbsHwSystemRedundentPowerSupplyStatus=cbsHwSystemRedundentPowerSupplyStatus, cbsHwSystemRedundentACPowerFeedStatus=cbsHwSystemRedundentACPowerFeedStatus, cbsHwSdpRemoteSlot=cbsHwSdpRemoteSlot, cbsHwSdpStatusTable=cbsHwSdpStatusTable, cbsDbhaLinkDown=cbsDbhaLinkDown, cbsHwSystemLowerFanTray=cbsHwSystemLowerFanTray, cbsHardware=cbsHardware, cbsHwModule3_3Voltage=cbsHwModule3_3Voltage, cbsHwModuleDiagnosticsRev=cbsHwModuleDiagnosticsRev, cbsHwModuleControlLinkA=cbsHwModuleControlLinkA, cbsHwUpperFanTrayRemoved=cbsHwUpperFanTrayRemoved, cbsHwSystemStatus=cbsHwSystemStatus, cbsHwModuleInTempAlarm=cbsHwModuleInTempAlarm, cbsHwModuleAccelCard1Present=cbsHwModuleAccelCard1Present, cbsHwModule2_5Voltage=cbsHwModule2_5Voltage, cbsHwModuleAccelCard2Present=cbsHwModuleAccelCard2Present, cbsHwModuleFPGA1_8Voltage=cbsHwModuleFPGA1_8Voltage, cbsHwModuleSerialNumber=cbsHwModuleSerialNumber, cbsHwModuleStatus=cbsHwModuleStatus, cbsHwModuleBootStrapRev=cbsHwModuleBootStrapRev, cbsHwModuleProductID=cbsHwModuleProductID, cbsHwModuleBoardRevision=cbsHwModuleBoardRevision, cbsHwPowerFeedFailed=cbsHwPowerFeedFailed, cbsHwSdpNpmState=cbsHwSdpNpmState, cbsDbhaLinkUp=cbsDbhaLinkUp, cbsHwModuleDuartAPresent=cbsHwModuleDuartAPresent, cbsModuleTempNormal=cbsModuleTempNormal, cbsHwSdpStatusEntry=cbsHwSdpStatusEntry, cbsHwLowerFanTrayInserted=cbsHwLowerFanTrayInserted, cbsFanStatus=cbsFanStatus, cbsHwSystemDCPowerFeedA=cbsHwSystemDCPowerFeedA, cbsHwComponentIndex=cbsHwComponentIndex, cbsHwModuleExhaustTempAlarm=cbsHwModuleExhaustTempAlarm, cbsHwSystemDCPowerFilterA=cbsHwSystemDCPowerFilterA, cbsHwSdpNpmSlot=cbsHwSdpNpmSlot, cbsHwPowerFeedRecovered=cbsHwPowerFeedRecovered, cbsHwModuleStatusEntry=cbsHwModuleStatusEntry, cbsHwModuleCpu2Temp=cbsHwModuleCpu2Temp, cbsHwUpperFanTrayInserted=cbsHwUpperFanTrayInserted, cbsHwModuleEntry=cbsHwModuleEntry, cbsHwSystemUpperFanTray=cbsHwSystemUpperFanTray, cbsHwPowerSupplyRecovered=cbsHwPowerSupplyRecovered, cbsHwFanFailed=cbsHwFanFailed, cbsHwLowerFanTrayRemoved=cbsHwLowerFanTrayRemoved, cbsHwSystem=cbsHwSystem, cbsHwModule1_8Voltage=cbsHwModule1_8Voltage, OperationalState=OperationalState, cbsHwModuleCpuTemp=cbsHwModuleCpuTemp, cbsHwPowerSupplyFailed=cbsHwPowerSupplyFailed, cbsHwFanRecovered=cbsHwFanRecovered, cbsFanStatusEntry=cbsFanStatusEntry, cbsHwSdpRemoteState=cbsHwSdpRemoteState, cbsHwSystemRedundentPowerFeedStatus=cbsHwSystemRedundentPowerFeedStatus, cbsHwModuleRDRAMSize=cbsHwModuleRDRAMSize, cbsHwModuleDiskBPresent=cbsHwModuleDiskBPresent, cbsHardwareMIB=cbsHardwareMIB, cbsHwModuleDescription=cbsHwModuleDescription, cbsHwSystemChassisTemp=cbsHwSystemChassisTemp, cbsHwSystemDCPowerFeedB=cbsHwSystemDCPowerFeedB, cbsHwModuleExhaustTemp=cbsHwModuleExhaustTemp, cbsFanGroupIndex=cbsFanGroupIndex, PYSNMP_MODULE_ID=cbsHardwareMIB, cbsHwModuleBootloaderRev=cbsHwModuleBootloaderRev, cbsHwComponentRevision=cbsHwComponentRevision, cbsHwModuleDuartBPresent=cbsHwModuleDuartBPresent, cbsHwSystemPowerType=cbsHwSystemPowerType, cbsHwModuleDiskAPresent=cbsHwModuleDiskAPresent, cbsHwModuleControlLinkB=cbsHwModuleControlLinkB, cbsHwSystemBackplaneRevision=cbsHwSystemBackplaneRevision)
