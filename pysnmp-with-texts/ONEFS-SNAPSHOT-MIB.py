#
# PySNMP MIB module ONEFS-SNAPSHOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEFS-SNAPSHOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
onefs, TimeTicks64 = mibBuilder.importSymbols("ONEFS-MIB", "onefs", "TimeTicks64")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Bits, Gauge32, TimeTicks, iso, NotificationType, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "iso", "NotificationType", "MibIdentifier", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString, MacAddress, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "PhysAddress")
oneFSss = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124, 3))
if mibBuilder.loadTexts: oneFSss.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: oneFSss.setOrganization('COMPANY_NAME')
if mibBuilder.loadTexts: oneFSss.setContactInfo('COMPANY_NAME Support phone: SUPPORT_PHONE Support email: SUPPORT_EMAIL ')
if mibBuilder.loadTexts: oneFSss.setDescription('This is the OneFS statistics MIB')
ssVersion = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssVersion.setStatus('current')
if mibBuilder.loadTexts: ssVersion.setDescription('The version number of this onefs snapshot')
ssLocalNodeId = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssLocalNodeId.setStatus('current')
if mibBuilder.loadTexts: ssLocalNodeId.setDescription('The array identification number of this device equivalent to the logical node number ')
ssTimeStart = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 3), TimeTicks64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssTimeStart.setStatus('current')
if mibBuilder.loadTexts: ssTimeStart.setDescription('Start time of this interval')
ssTimeEnd = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 4), TimeTicks64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssTimeEnd.setStatus('current')
if mibBuilder.loadTexts: ssTimeEnd.setDescription('End time of this interval')
ssGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 3, 5))
ssNodeInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 3, 6))
ssDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 3, 5, 1))
ssNet = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2))
ssSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 3, 5, 3))
ssFreeBlocks = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssFreeBlocks.setStatus('current')
if mibBuilder.loadTexts: ssFreeBlocks.setDescription('Free Blocks on this cluster')
ssTotalBlocks = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssTotalBlocks.setStatus('current')
if mibBuilder.loadTexts: ssTotalBlocks.setDescription('Total number of blocks in the cluster')
ssAvailableBlocks = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssAvailableBlocks.setStatus('current')
if mibBuilder.loadTexts: ssAvailableBlocks.setDescription('Number of available blocks in the cluster')
ssBlockSize = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssBlockSize.setStatus('current')
if mibBuilder.loadTexts: ssBlockSize.setDescription('Size of the oneFS blocks')
ssNetBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNetBytesIn.setStatus('current')
if mibBuilder.loadTexts: ssNetBytesIn.setDescription('Total Number of bytes into the cluster')
ssNetBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNetBytesOut.setStatus('current')
if mibBuilder.loadTexts: ssNetBytesOut.setDescription('Total number of bytes out of the cluster')
ssFilesystemBytesIn = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssFilesystemBytesIn.setStatus('current')
if mibBuilder.loadTexts: ssFilesystemBytesIn.setDescription('Number of bytes into the filesystem')
ssFilesystemBytesOut = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssFilesystemBytesOut.setStatus('current')
if mibBuilder.loadTexts: ssFilesystemBytesOut.setDescription('Number of bytes out of the filesystem')
ssNetBitsPerSecIn = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNetBitsPerSecIn.setStatus('current')
if mibBuilder.loadTexts: ssNetBitsPerSecIn.setDescription('Total bits/sec into the cluster')
ssNetBitsPerSecOut = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNetBitsPerSecOut.setStatus('current')
if mibBuilder.loadTexts: ssNetBitsPerSecOut.setDescription('Total bits/sec out of the cluster')
ssFilesystemBitsPerSecIn = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssFilesystemBitsPerSecIn.setStatus('current')
if mibBuilder.loadTexts: ssFilesystemBitsPerSecIn.setDescription('Bits/sec into the filesystem')
ssFilesystemBitsPerSecOut = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 2, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssFilesystemBitsPerSecOut.setStatus('current')
if mibBuilder.loadTexts: ssFilesystemBitsPerSecOut.setDescription('Bits/sec out of the filesystem')
ssClusterName = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssClusterName.setStatus('current')
if mibBuilder.loadTexts: ssClusterName.setDescription('The cluster name')
ssClusterHealth = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssClusterHealth.setStatus('current')
if mibBuilder.loadTexts: ssClusterHealth.setDescription('Health Status of Cluster')
ssConfiguredNodes = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssConfiguredNodes.setStatus('current')
if mibBuilder.loadTexts: ssConfiguredNodes.setDescription('The number of devices currently configured to be in the cluster ')
ssOnlineNodes = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 5, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssOnlineNodes.setStatus('current')
if mibBuilder.loadTexts: ssOnlineNodes.setDescription('The number of devices in the cluster currently online')
ssNodeTable = MibTable((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1), )
if mibBuilder.loadTexts: ssNodeTable.setStatus('current')
if mibBuilder.loadTexts: ssNodeTable.setDescription('Table of oneFS machines')
ssNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1), ).setIndexNames((0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"))
if mibBuilder.loadTexts: ssNodeEntry.setStatus('current')
if mibBuilder.loadTexts: ssNodeEntry.setDescription('Table of oneFS machines')
ssNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeIndex.setStatus('current')
if mibBuilder.loadTexts: ssNodeIndex.setDescription('The logical node number of this device ')
ssNodeFreeBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeFreeBlocks.setStatus('current')
if mibBuilder.loadTexts: ssNodeFreeBlocks.setDescription('The number of oneFS free blocks equivalent to sysctl efs.lbm.free_blocks on this machine ')
ssNodeTotalBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeTotalBlocks.setStatus('current')
if mibBuilder.loadTexts: ssNodeTotalBlocks.setDescription('The number of oneFS total blocks. Equivalent to sysctl efs.lbm.total_blocks on this machine')
ssNodeAvailBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeAvailBlocks.setStatus('current')
if mibBuilder.loadTexts: ssNodeAvailBlocks.setDescription('The number of oneFS available blocks. Equivalent to sysctl efs.lbm.free_blocks on this machine')
ssNodeLnn = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeLnn.setStatus('current')
if mibBuilder.loadTexts: ssNodeLnn.setDescription('The logical node number of this device.')
ssNodeDiskless = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeDiskless.setStatus('current')
if mibBuilder.loadTexts: ssNodeDiskless.setDescription('The diskless state of this device.')
ssNodeNetBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNetBytesIn.setStatus('current')
if mibBuilder.loadTexts: ssNodeNetBytesIn.setDescription('Total Network traffic into the device not including local overhead. ')
ssNodeNetBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNetBytesOut.setStatus('current')
if mibBuilder.loadTexts: ssNodeNetBytesOut.setDescription('Total Network traffic into the device not including local overhead. ')
ssNodeMACaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 9), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeMACaddress.setStatus('current')
if mibBuilder.loadTexts: ssNodeMACaddress.setDescription('MacAddress of the device')
ssNodeIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeIPaddress.setStatus('current')
if mibBuilder.loadTexts: ssNodeIPaddress.setDescription('Internal IP address of the device')
ssNodeVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeVersion.setStatus('current')
if mibBuilder.loadTexts: ssNodeVersion.setDescription('Isilon IQ version')
ssNodeBoottime = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 12), TimeTicks64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeBoottime.setStatus('current')
if mibBuilder.loadTexts: ssNodeBoottime.setDescription('')
ssNodeHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeHealth.setStatus('current')
if mibBuilder.loadTexts: ssNodeHealth.setDescription('')
ssNodeCPUload = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUload.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUload.setDescription('Local CPU load based on the kern.cp_time sysctl')
ssNodeFilesystemBytesIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeFilesystemBytesIn.setStatus('current')
if mibBuilder.loadTexts: ssNodeFilesystemBytesIn.setDescription('Number of bytes into the filesystem')
ssNodeFilesystemBytesOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeFilesystemBytesOut.setStatus('current')
if mibBuilder.loadTexts: ssNodeFilesystemBytesOut.setDescription('Number of bytes out of the filesystem')
ssNodeNumberOfDisks = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNumberOfDisks.setStatus('current')
if mibBuilder.loadTexts: ssNodeNumberOfDisks.setDescription('Number of disks on the appliance')
ssNodeNumberOfSensors = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNumberOfSensors.setStatus('current')
if mibBuilder.loadTexts: ssNodeNumberOfSensors.setDescription('Number of hardware sensors on the appliance')
ssNodeNetBitsPerSecIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNetBitsPerSecIn.setStatus('current')
if mibBuilder.loadTexts: ssNodeNetBitsPerSecIn.setDescription('')
ssNodeNetBitsPerSecOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeNetBitsPerSecOut.setStatus('current')
if mibBuilder.loadTexts: ssNodeNetBitsPerSecOut.setDescription('')
ssNodeFilesystemBitsPerSecIn = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeFilesystemBitsPerSecIn.setStatus('current')
if mibBuilder.loadTexts: ssNodeFilesystemBitsPerSecIn.setDescription('')
ssNodeFilesystemBitsPerSecOut = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeFilesystemBitsPerSecOut.setStatus('current')
if mibBuilder.loadTexts: ssNodeFilesystemBitsPerSecOut.setDescription('')
ssNodeCPUuser = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUuser.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUuser.setDescription('Local CPU % used by user ')
ssNodeCPUnice = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUnice.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUnice.setDescription("Local CPU % used by nice'd proccesses")
ssNodeCPUsystem = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUsystem.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUsystem.setDescription('Local CPU % used by system ')
ssNodeCPUinterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 27), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUinterrupt.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUinterrupt.setDescription('Local CPU % used by interrupts ')
ssNodeCPUidle = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeCPUidle.setStatus('current')
if mibBuilder.loadTexts: ssNodeCPUidle.setDescription('Local CPU % idle')
ssNodeDevId = MibScalar((1, 3, 6, 1, 4, 1, 12124, 3, 6, 1, 1, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssNodeDevId.setStatus('current')
if mibBuilder.loadTexts: ssNodeDevId.setDescription('The array identification number of this device equivalent to sysctl efs.rbm.array_id on this machine ')
ssDiskInfoTable = MibTable((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2), )
if mibBuilder.loadTexts: ssDiskInfoTable.setStatus('current')
if mibBuilder.loadTexts: ssDiskInfoTable.setDescription('Table of oneFS machines')
ssDiskInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1), ).setIndexNames((0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"), (0, "ONEFS-SNAPSHOT-MIB", "ssDiskIndex"))
if mibBuilder.loadTexts: ssDiskInfoEntry.setStatus('current')
if mibBuilder.loadTexts: ssDiskInfoEntry.setDescription('Table of oneFS machines')
ssDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskIndex.setStatus('current')
if mibBuilder.loadTexts: ssDiskIndex.setDescription('Index of the ssDiskInfoTable, also the disk number')
ssDiskName = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskName.setStatus('current')
if mibBuilder.loadTexts: ssDiskName.setDescription('Name of the disk i.e. ad0')
ssDiskHealth = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("red", 0), ("green", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskHealth.setStatus('current')
if mibBuilder.loadTexts: ssDiskHealth.setDescription('Current status of a disk')
ssDiskBytesRead = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskBytesRead.setStatus('current')
if mibBuilder.loadTexts: ssDiskBytesRead.setDescription('Bytes read on this disk')
ssDiskBytesWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskBytesWritten.setStatus('current')
if mibBuilder.loadTexts: ssDiskBytesWritten.setDescription('Bytes written on this disk')
ssDiskNumXfers = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskNumXfers.setStatus('current')
if mibBuilder.loadTexts: ssDiskNumXfers.setDescription('Number of transfers to and from this disk')
ssDiskBitsPerSecRead = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskBitsPerSecRead.setStatus('current')
if mibBuilder.loadTexts: ssDiskBitsPerSecRead.setDescription('Bits per sec read from this disk')
ssDiskBitsPerSecWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskBitsPerSecWritten.setStatus('current')
if mibBuilder.loadTexts: ssDiskBitsPerSecWritten.setDescription('Bits per sec written on this disk')
ssDiskXfersPerSec = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssDiskXfersPerSec.setStatus('current')
if mibBuilder.loadTexts: ssDiskXfersPerSec.setDescription('Number of thousandths of transfers per second to and from this disk ')
ssSensorInfoTable = MibTable((1, 3, 6, 1, 4, 1, 12124, 3, 6, 3), )
if mibBuilder.loadTexts: ssSensorInfoTable.setStatus('current')
if mibBuilder.loadTexts: ssSensorInfoTable.setDescription('Table of oneFS machines')
ssSensorInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1), ).setIndexNames((0, "ONEFS-SNAPSHOT-MIB", "ssNodeIndex"), (0, "ONEFS-SNAPSHOT-MIB", "ssDiskIndex"))
if mibBuilder.loadTexts: ssSensorInfoEntry.setStatus('current')
if mibBuilder.loadTexts: ssSensorInfoEntry.setDescription('Table of oneFS machines')
ssSensorDescriptionName = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSensorDescriptionName.setStatus('current')
if mibBuilder.loadTexts: ssSensorDescriptionName.setDescription('Description of the hardware sensor; e.g. Temp Front Panel')
ssSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSensorType.setStatus('current')
if mibBuilder.loadTexts: ssSensorType.setDescription('Type of hardware sensor: fan, voltage, or temperature.')
ssSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 12124, 3, 6, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ssSensorValue.setStatus('current')
if mibBuilder.loadTexts: ssSensorValue.setDescription('Current value of sensor.')
mibBuilder.exportSymbols("ONEFS-SNAPSHOT-MIB", ssNodeIPaddress=ssNodeIPaddress, ssSensorType=ssSensorType, ssDiskBytesRead=ssDiskBytesRead, ssDiskName=ssDiskName, ssNodeDevId=ssNodeDevId, ssDiskBytesWritten=ssDiskBytesWritten, ssNodeNetBitsPerSecIn=ssNodeNetBitsPerSecIn, ssNodeCPUuser=ssNodeCPUuser, ssFilesystemBytesOut=ssFilesystemBytesOut, ssNodeTotalBlocks=ssNodeTotalBlocks, oneFSss=oneFSss, ssFilesystemBytesIn=ssFilesystemBytesIn, ssNodeEntry=ssNodeEntry, ssSensorDescriptionName=ssSensorDescriptionName, ssGlobal=ssGlobal, ssLocalNodeId=ssLocalNodeId, ssNodeTable=ssNodeTable, ssNodeAvailBlocks=ssNodeAvailBlocks, ssNodeFilesystemBytesOut=ssNodeFilesystemBytesOut, ssNodeFilesystemBytesIn=ssNodeFilesystemBytesIn, ssClusterHealth=ssClusterHealth, ssNodeIndex=ssNodeIndex, ssNodeDiskless=ssNodeDiskless, ssOnlineNodes=ssOnlineNodes, ssNodeFreeBlocks=ssNodeFreeBlocks, ssNodeNetBitsPerSecOut=ssNodeNetBitsPerSecOut, ssNodeMACaddress=ssNodeMACaddress, ssDiskInfoEntry=ssDiskInfoEntry, ssFreeBlocks=ssFreeBlocks, ssNodeHealth=ssNodeHealth, ssDiskIndex=ssDiskIndex, PYSNMP_MODULE_ID=oneFSss, ssDiskHealth=ssDiskHealth, ssDiskXfersPerSec=ssDiskXfersPerSec, ssBlockSize=ssBlockSize, ssAvailableBlocks=ssAvailableBlocks, ssNetBytesOut=ssNetBytesOut, ssTotalBlocks=ssTotalBlocks, ssConfiguredNodes=ssConfiguredNodes, ssNodeBoottime=ssNodeBoottime, ssDiskBitsPerSecWritten=ssDiskBitsPerSecWritten, ssVersion=ssVersion, ssNodeVersion=ssNodeVersion, ssNet=ssNet, ssNodeCPUload=ssNodeCPUload, ssNodeNetBytesIn=ssNodeNetBytesIn, ssNetBitsPerSecOut=ssNetBitsPerSecOut, ssNetBytesIn=ssNetBytesIn, ssNodeFilesystemBitsPerSecOut=ssNodeFilesystemBitsPerSecOut, ssTimeEnd=ssTimeEnd, ssNodeFilesystemBitsPerSecIn=ssNodeFilesystemBitsPerSecIn, ssNodeNumberOfSensors=ssNodeNumberOfSensors, ssSensorValue=ssSensorValue, ssNodeCPUinterrupt=ssNodeCPUinterrupt, ssSystem=ssSystem, ssNodeCPUnice=ssNodeCPUnice, ssDiskBitsPerSecRead=ssDiskBitsPerSecRead, ssSensorInfoTable=ssSensorInfoTable, ssNodeInfo=ssNodeInfo, ssNetBitsPerSecIn=ssNetBitsPerSecIn, ssNodeNetBytesOut=ssNodeNetBytesOut, ssDisk=ssDisk, ssNodeCPUidle=ssNodeCPUidle, ssSensorInfoEntry=ssSensorInfoEntry, ssFilesystemBitsPerSecOut=ssFilesystemBitsPerSecOut, ssClusterName=ssClusterName, ssNodeCPUsystem=ssNodeCPUsystem, ssDiskNumXfers=ssDiskNumXfers, ssNodeLnn=ssNodeLnn, ssDiskInfoTable=ssDiskInfoTable, ssTimeStart=ssTimeStart, ssNodeNumberOfDisks=ssNodeNumberOfDisks, ssFilesystemBitsPerSecIn=ssFilesystemBitsPerSecIn)
