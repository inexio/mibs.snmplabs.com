#
# PySNMP MIB module HUAWEI-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-CPU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hwSlotIndex, hwFrameIndex = mibBuilder.importSymbols("HUAWEI-DEVICE-MIB", "hwSlotIndex", "hwFrameIndex")
huaweiUtility, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiUtility")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Counter64, ObjectIdentity, TimeTicks, Unsigned32, Integer32, Counter32, iso, ModuleIdentity, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "Unsigned32", "Integer32", "Counter32", "iso", "ModuleIdentity", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwDev = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 3))
if mibBuilder.loadTexts: hwDev.setLastUpdated('200406280900Z')
if mibBuilder.loadTexts: hwDev.setOrganization('Fix-Net Dept, Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwDev.setContactInfo('Block 4, R&D Building, Huawei Longgang Production Base, Shenzhen, P.R.C. http://www.huawei.com Zip:518057 ')
if mibBuilder.loadTexts: hwDev.setDescription('huawei device mib.')
hwCpuDevTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4), )
if mibBuilder.loadTexts: hwCpuDevTable.setStatus('current')
if mibBuilder.loadTexts: hwCpuDevTable.setDescription(' This table provides the information of CPU usage statistics of device in the period of last 5 seconds, 1 minute,or 5 minutes. ')
hwCpuDevEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1), ).setIndexNames((0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"), (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"), (0, "HUAWEI-CPU-MIB", "hwCpuDevIndex"))
if mibBuilder.loadTexts: hwCpuDevEntry.setStatus('current')
if mibBuilder.loadTexts: hwCpuDevEntry.setDescription(' The Entries of hwCpuDevTable. The hwCpuDevTable is indexed by hwFrameIndex, hwSlotIndex and hwCpuDevIndex. hwFrameIndex - the index of frame of the device. for example, hwFrameIndex equals 0 in NE16. hwSlotIndex - the slot number of the device, the MAX value varies with different devices. hwCpuDevIndex - for the purpose of extension.In single CPU devices (NE16,eg.), hwCpuDevIndex equals 0.')
hwCpuDevIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: hwCpuDevIndex.setStatus('current')
if mibBuilder.loadTexts: hwCpuDevIndex.setDescription(' The object is used only for the purpose of extension. For single-CPU devices, the value of this object equals 0. ')
hwCpuDevDuty = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCpuDevDuty.setStatus('current')
if mibBuilder.loadTexts: hwCpuDevDuty.setDescription(' The value of this object identifies the average CPU occupancy of a board or an entity.')
hwAvgDuty1min = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAvgDuty1min.setStatus('current')
if mibBuilder.loadTexts: hwAvgDuty1min.setDescription(' The value of this object identifies the average CPU occupancy of a board or an entity in the last one minute before you access the object. ')
hwAvgDuty5min = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 6, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwAvgDuty5min.setStatus('current')
if mibBuilder.loadTexts: hwAvgDuty5min.setDescription(' The value of this object identifies the average CPU occupancy of a board or an entity in the last five minutes before you access the object. ')
mibBuilder.exportSymbols("HUAWEI-CPU-MIB", hwAvgDuty1min=hwAvgDuty1min, hwAvgDuty5min=hwAvgDuty5min, hwCpuDevIndex=hwCpuDevIndex, hwCpuDevDuty=hwCpuDevDuty, PYSNMP_MODULE_ID=hwDev, hwCpuDevTable=hwCpuDevTable, hwCpuDevEntry=hwCpuDevEntry, hwDev=hwDev)
