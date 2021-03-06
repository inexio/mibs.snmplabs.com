#
# PySNMP MIB module CIG-SERVERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIG-SERVERS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Counter64, iso, TimeTicks, ModuleIdentity, MibIdentifier, Counter32, Integer32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Counter64", "iso", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter32", "Integer32", "NotificationType", "ObjectIdentity")
TruthValue, RowStatus, DisplayString, DateAndTime, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "DateAndTime", "TextualConvention", "TimeInterval")
cigServers = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16))
if mibBuilder.loadTexts: cigServers.setLastUpdated('200405180701Z')
if mibBuilder.loadTexts: cigServers.setOrganization('Avaya')
avaya = MibIdentifier((1, 3, 6, 1, 4, 1, 6889))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2))
lsg = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1))
cigTftpServers = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1))
cigDhcpServers = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2))
cigTftpServersNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0))
cigTftpServersDownloadFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0, 1)).setObjects(("CIG-SERVERS-MIB", "cigTftpServersNotificationClientIpAddr"), ("CIG-SERVERS-MIB", "cigTftpServersNotificationFilename"), ("CIG-SERVERS-MIB", "cigTftpServersNotificationErrorString"))
if mibBuilder.loadTexts: cigTftpServersDownloadFailureTrap.setStatus('current')
cigTftpServersUploadFailureTrap = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 0, 2)).setObjects(("CIG-SERVERS-MIB", "cigTftpServersNotificationClientIpAddr"), ("CIG-SERVERS-MIB", "cigTftpServersNotificationFilename"), ("CIG-SERVERS-MIB", "cigTftpServersNotificationErrorString"))
if mibBuilder.loadTexts: cigTftpServersUploadFailureTrap.setStatus('current')
cigTftpServersGenConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1))
cigTftpServersMode = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigTftpServersMode.setStatus('current')
cigTftpServersResetStatCounters = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigTftpServersResetStatCounters.setStatus('current')
cigTftpServersMemoryAllocation = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2))
cigTftpServersTotalBytesUsedInNvram = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersTotalBytesUsedInNvram.setStatus('current')
cigTftpServersTotalBytesCapacityInNvram = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 2), Unsigned32().clone(131072)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersTotalBytesCapacityInNvram.setStatus('current')
cigTftpServersTotalBytesUsedInRam = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersTotalBytesUsedInRam.setStatus('current')
cigTftpServersTotalBytesCapacityInRam = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 2, 4), Unsigned32().clone(20971520)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersTotalBytesCapacityInRam.setStatus('current')
cigTftpServersGenStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3))
cigTftpServersSuccessfulDownloads = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersSuccessfulDownloads.setStatus('current')
cigTftpServersNotDefinedErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersNotDefinedErrors.setStatus('current')
cigTftpServersFileNotFoundErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersFileNotFoundErrors.setStatus('current')
cigTftpServersAccessViolationErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersAccessViolationErrors.setStatus('current')
cigTftpServersDiskFullErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersDiskFullErrors.setStatus('current')
cigTftpServersIllegalTFTPOperationErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersIllegalTFTPOperationErrors.setStatus('current')
cigTftpServersUnknownTransferIdErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersUnknownTransferIdErrors.setStatus('current')
cigTftpServersFileAlreadyExistsErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersFileAlreadyExistsErrors.setStatus('current')
cigTftpServersNoSuchUserErrors = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersNoSuchUserErrors.setStatus('current')
cigTftpServersDownloadTimeouts = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 3, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigTftpServersDownloadTimeouts.setStatus('current')
cigTftpServersNotificationPacket = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4))
cigTftpServersNotificationClientIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigTftpServersNotificationClientIpAddr.setStatus('current')
cigTftpServersNotificationFilename = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigTftpServersNotificationFilename.setStatus('current')
cigTftpServersNotificationErrorString = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 1, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigTftpServersNotificationErrorString.setStatus('current')
cigDhcpServersNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0))
cigDhcpServersClientConflictDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 1)).setObjects(("CIG-SERVERS-MIB", "cigDhcpServersNotificationIpAddr"), ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientHostName"), ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"), ("CIG-SERVERS-MIB", "cigDhcpServersNotificationConflictDetectionMethod"))
if mibBuilder.loadTexts: cigDhcpServersClientConflictDetectionTrap.setStatus('current')
cigDhcpServersServerNacksTrap = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 2)).setObjects(("CIG-SERVERS-MIB", "cigDhcpServersNotificationIpAddr"), ("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"))
if mibBuilder.loadTexts: cigDhcpServersServerNacksTrap.setStatus('current')
cigDhcpServersNoIpAddressLeft = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 0, 3)).setObjects(("CIG-SERVERS-MIB", "cigDhcpServersNotificationClientIdentifier"), ("CIG-SERVERS-MIB", "cigDhcpServersNotificationPoolNetwork"))
if mibBuilder.loadTexts: cigDhcpServersNoIpAddressLeft.setStatus('current')
cigDhcpServersGenConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1))
cigDhcpServersMode = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersMode.setStatus('current')
cigDhcpServersResetStatCounters = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersResetStatCounters.setStatus('current')
cigDhcpServersPingDetectionMode = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPingDetectionMode.setStatus('current')
cigDhcpServersPingDetectionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 1, 4), Unsigned32().clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPingDetectionTimeout.setStatus('current')
cigDhcpServersPool = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2))
cigDhcpServersPoolTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1), )
if mibBuilder.loadTexts: cigDhcpServersPoolTable.setStatus('current')
cigDhcpServersPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1), ).setIndexNames((0, "CIG-SERVERS-MIB", "cigDhcpServersPoolIndex"))
if mibBuilder.loadTexts: cigDhcpServersPoolEntry.setStatus('current')
cigDhcpServersPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersPoolIndex.setStatus('current')
cigDhcpServersPoolStartIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolStartIPAddr.setStatus('current')
cigDhcpServersPoolEndIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolEndIPAddr.setStatus('current')
cigDhcpServersPoolMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolMode.setStatus('current')
cigDhcpServersPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15)).clone('Dhcp Pool #')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolName.setStatus('current')
cigDhcpServersPoolClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolClientID.setStatus('current')
cigDhcpServersPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 7), Unsigned32().clone(691200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolLeaseTime.setStatus('current')
cigDhcpServersPoolBootFile = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolBootFile.setStatus('current')
cigDhcpServersPoolNextServer = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 9), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolNextServer.setStatus('current')
cigDhcpServersPoolSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 10), IpAddress().clone(hexValue="ffffff00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolSubnetMask.setStatus('current')
cigDhcpServersPoolDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 145))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolDefaultGateway.setStatus('current')
cigDhcpServersPoolDnsServer = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 145))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolDnsServer.setStatus('current')
cigDhcpServersPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolDomainName.setStatus('current')
cigDhcpServersPoolServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolServerName.setStatus('current')
cigDhcpServersPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 1, 1, 15), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersPoolRowStatus.setStatus('current')
cigDhcpServersPoolGenOptionTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2), )
if mibBuilder.loadTexts: cigDhcpServersPoolGenOptionTable.setStatus('current')
cigDhcpServersPoolGenOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1), ).setIndexNames((0, "CIG-SERVERS-MIB", "cigDhcpServersOptionPoolIndex"), (0, "CIG-SERVERS-MIB", "cigDhcpServersOptionIndex"))
if mibBuilder.loadTexts: cigDhcpServersPoolGenOptionEntry.setStatus('current')
cigDhcpServersOptionPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersOptionPoolIndex.setStatus('current')
cigDhcpServersOptionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersOptionIndex.setStatus('current')
cigDhcpServersOptionName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone('Option #')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersOptionName.setStatus('current')
cigDhcpServersOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2), ("ipAddresses", 3), ("integer", 4), ("word", 5))).clone('hex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersOptionType.setStatus('current')
cigDhcpServersOptionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersOptionValue.setStatus('current')
cigDhcpServersOptionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersOptionRowStatus.setStatus('current')
cigDhcpServersPoolVendorSpecificOptionTable = MibTable((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3), )
if mibBuilder.loadTexts: cigDhcpServersPoolVendorSpecificOptionTable.setStatus('current')
cigDhcpServersPoolVendorSpecificOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1), ).setIndexNames((0, "CIG-SERVERS-MIB", "cigDhcpServersVendorSpecificOptionPoolIndex"), (0, "CIG-SERVERS-MIB", "cigDhcpServersVendorSpecificOptionIndex"))
if mibBuilder.loadTexts: cigDhcpServersPoolVendorSpecificOptionEntry.setStatus('current')
cigDhcpServersVendorSpecificOptionPoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionPoolIndex.setStatus('current')
cigDhcpServersVendorSpecificOptionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionIndex.setStatus('current')
cigDhcpServersVendorSpecificOptionName = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)).clone('Vendor Specific Option #')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionName.setStatus('current')
cigDhcpServersVendorSpecificClassIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificClassIdentifier.setStatus('current')
cigDhcpServersVendorSpecificOptionType = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2))).clone('hex')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionType.setStatus('current')
cigDhcpServersVendorSpecificOptionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionValue.setStatus('current')
cigDhcpServersVendorSpecificOptionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 2, 3, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cigDhcpServersVendorSpecificOptionRowStatus.setStatus('current')
cigDhcpServersGenStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3))
cigDhcpServersBootRequests = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersBootRequests.setStatus('current')
cigDhcpServersDhcpDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpDiscovers.setStatus('current')
cigDhcpServersDhcpRequests = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpRequests.setStatus('current')
cigDhcpServersDhcpDeclines = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpDeclines.setStatus('current')
cigDhcpServersDhcpReleases = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpReleases.setStatus('current')
cigDhcpServersDhcpInforms = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpInforms.setStatus('current')
cigDhcpServersBootReplies = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersBootReplies.setStatus('current')
cigDhcpServersDhcpOffers = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpOffers.setStatus('current')
cigDhcpServersDhcpAcks = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpAcks.setStatus('current')
cigDhcpServersDhcpNacks = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 3, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cigDhcpServersDhcpNacks.setStatus('current')
cigDhcpServersNotificationPacket = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4))
cigDhcpServersNotificationIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 1), IpAddress().clone(hexValue="00000000")).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigDhcpServersNotificationIpAddr.setStatus('current')
cigDhcpServersNotificationClientIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="01000000000000")).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigDhcpServersNotificationClientIdentifier.setStatus('current')
cigDhcpServersNotificationClientHostName = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigDhcpServersNotificationClientHostName.setStatus('current')
cigDhcpServersNotificationConflictDetectionMethod = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ping", 1), ("gratuitousArp", 2), ("notSupported", 255))).clone('notSupported')).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigDhcpServersNotificationConflictDetectionMethod.setStatus('current')
cigDhcpServersNotificationPoolNetwork = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 1, 16, 2, 4, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cigDhcpServersNotificationPoolNetwork.setStatus('current')
mibBuilder.exportSymbols("CIG-SERVERS-MIB", cigTftpServersUploadFailureTrap=cigTftpServersUploadFailureTrap, cigTftpServersResetStatCounters=cigTftpServersResetStatCounters, cigTftpServersNotificationErrorString=cigTftpServersNotificationErrorString, cigDhcpServersPoolBootFile=cigDhcpServersPoolBootFile, cigDhcpServersOptionType=cigDhcpServersOptionType, cigTftpServersDownloadFailureTrap=cigTftpServersDownloadFailureTrap, cigDhcpServersNotificationPoolNetwork=cigDhcpServersNotificationPoolNetwork, cigTftpServersNotificationPacket=cigTftpServersNotificationPacket, cigTftpServersAccessViolationErrors=cigTftpServersAccessViolationErrors, cigDhcpServersPoolDefaultGateway=cigDhcpServersPoolDefaultGateway, cigDhcpServersPoolTable=cigDhcpServersPoolTable, cigTftpServersNotDefinedErrors=cigTftpServersNotDefinedErrors, cigDhcpServersDhcpRequests=cigDhcpServersDhcpRequests, cigDhcpServersPoolLeaseTime=cigDhcpServersPoolLeaseTime, cigTftpServersGenStats=cigTftpServersGenStats, cigTftpServersDiskFullErrors=cigTftpServersDiskFullErrors, cigDhcpServersNotificationConflictDetectionMethod=cigDhcpServersNotificationConflictDetectionMethod, cigDhcpServersResetStatCounters=cigDhcpServersResetStatCounters, cigDhcpServersPoolDnsServer=cigDhcpServersPoolDnsServer, cigDhcpServersPoolServerName=cigDhcpServersPoolServerName, cigDhcpServersPoolVendorSpecificOptionTable=cigDhcpServersPoolVendorSpecificOptionTable, cigTftpServersNotificationFilename=cigTftpServersNotificationFilename, cigDhcpServersPoolClientID=cigDhcpServersPoolClientID, cigDhcpServersPingDetectionTimeout=cigDhcpServersPingDetectionTimeout, cigDhcpServersPoolRowStatus=cigDhcpServersPoolRowStatus, cigDhcpServersNoIpAddressLeft=cigDhcpServersNoIpAddressLeft, cigDhcpServersPoolName=cigDhcpServersPoolName, mibs=mibs, cigDhcpServersPoolMode=cigDhcpServersPoolMode, cigTftpServersUnknownTransferIdErrors=cigTftpServersUnknownTransferIdErrors, cigTftpServersNotificationClientIpAddr=cigTftpServersNotificationClientIpAddr, cigDhcpServersVendorSpecificOptionIndex=cigDhcpServersVendorSpecificOptionIndex, cigDhcpServersBootRequests=cigDhcpServersBootRequests, cigServers=cigServers, cigTftpServersTotalBytesCapacityInRam=cigTftpServersTotalBytesCapacityInRam, cigDhcpServersOptionName=cigDhcpServersOptionName, cigDhcpServersPool=cigDhcpServersPool, cigDhcpServersPoolGenOptionEntry=cigDhcpServersPoolGenOptionEntry, cigDhcpServersGenConfig=cigDhcpServersGenConfig, cigDhcpServersClientConflictDetectionTrap=cigDhcpServersClientConflictDetectionTrap, cigDhcpServersNotificationPacket=cigDhcpServersNotificationPacket, cigDhcpServers=cigDhcpServers, cigTftpServersIllegalTFTPOperationErrors=cigTftpServersIllegalTFTPOperationErrors, cigDhcpServersPoolStartIPAddr=cigDhcpServersPoolStartIPAddr, cigTftpServersMode=cigTftpServersMode, cigDhcpServersNotificationIpAddr=cigDhcpServersNotificationIpAddr, cigTftpServersGenConfig=cigTftpServersGenConfig, cigTftpServersSuccessfulDownloads=cigTftpServersSuccessfulDownloads, cigDhcpServersVendorSpecificOptionRowStatus=cigDhcpServersVendorSpecificOptionRowStatus, PYSNMP_MODULE_ID=cigServers, cigTftpServersTotalBytesUsedInRam=cigTftpServersTotalBytesUsedInRam, cigTftpServersFileAlreadyExistsErrors=cigTftpServersFileAlreadyExistsErrors, cigDhcpServersDhcpOffers=cigDhcpServersDhcpOffers, cigTftpServersFileNotFoundErrors=cigTftpServersFileNotFoundErrors, cigDhcpServersDhcpNacks=cigDhcpServersDhcpNacks, cigDhcpServersOptionIndex=cigDhcpServersOptionIndex, cigDhcpServersDhcpInforms=cigDhcpServersDhcpInforms, cigDhcpServersOptionPoolIndex=cigDhcpServersOptionPoolIndex, cigDhcpServersVendorSpecificOptionName=cigDhcpServersVendorSpecificOptionName, cigDhcpServersPoolSubnetMask=cigDhcpServersPoolSubnetMask, cigDhcpServersPoolNextServer=cigDhcpServersPoolNextServer, cigDhcpServersVendorSpecificOptionPoolIndex=cigDhcpServersVendorSpecificOptionPoolIndex, cigDhcpServersPoolEndIPAddr=cigDhcpServersPoolEndIPAddr, cigDhcpServersPoolGenOptionTable=cigDhcpServersPoolGenOptionTable, cigDhcpServersGenStats=cigDhcpServersGenStats, cigTftpServersTotalBytesCapacityInNvram=cigTftpServersTotalBytesCapacityInNvram, cigDhcpServersDhcpAcks=cigDhcpServersDhcpAcks, cigDhcpServersOptionValue=cigDhcpServersOptionValue, cigDhcpServersBootReplies=cigDhcpServersBootReplies, cigDhcpServersNotificationClientIdentifier=cigDhcpServersNotificationClientIdentifier, lsg=lsg, cigTftpServersDownloadTimeouts=cigTftpServersDownloadTimeouts, cigTftpServersNotification=cigTftpServersNotification, cigDhcpServersNotificationClientHostName=cigDhcpServersNotificationClientHostName, cigTftpServersTotalBytesUsedInNvram=cigTftpServersTotalBytesUsedInNvram, cigDhcpServersPingDetectionMode=cigDhcpServersPingDetectionMode, cigDhcpServersDhcpDiscovers=cigDhcpServersDhcpDiscovers, cigDhcpServersVendorSpecificOptionType=cigDhcpServersVendorSpecificOptionType, cigDhcpServersPoolEntry=cigDhcpServersPoolEntry, cigDhcpServersPoolDomainName=cigDhcpServersPoolDomainName, cigDhcpServersNotification=cigDhcpServersNotification, cigDhcpServersPoolVendorSpecificOptionEntry=cigDhcpServersPoolVendorSpecificOptionEntry, avaya=avaya, cigTftpServersMemoryAllocation=cigTftpServersMemoryAllocation, cigDhcpServersServerNacksTrap=cigDhcpServersServerNacksTrap, cigDhcpServersMode=cigDhcpServersMode, cigTftpServers=cigTftpServers, cigDhcpServersPoolIndex=cigDhcpServersPoolIndex, cigDhcpServersDhcpDeclines=cigDhcpServersDhcpDeclines, cigDhcpServersOptionRowStatus=cigDhcpServersOptionRowStatus, cigDhcpServersDhcpReleases=cigDhcpServersDhcpReleases, cigDhcpServersVendorSpecificOptionValue=cigDhcpServersVendorSpecificOptionValue, cigDhcpServersVendorSpecificClassIdentifier=cigDhcpServersVendorSpecificClassIdentifier, cigTftpServersNoSuchUserErrors=cigTftpServersNoSuchUserErrors)
