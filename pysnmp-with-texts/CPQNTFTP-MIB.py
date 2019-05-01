#
# PySNMP MIB module CPQNTFTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQNTFTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
CpqnRowStatus, = mibBuilder.importSymbols("CPQNUNIF-MIB", "CpqnRowStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, NotificationType, enterprises, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Unsigned32, Gauge32, IpAddress, Counter32, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "NotificationType", "enterprises", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Unsigned32", "Gauge32", "IpAddress", "Counter32", "MibIdentifier", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqnCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 121))
cpqnTftpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 121, 9))
cpqnTftpInitiate = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-transfer-ipr", 1), ("transfer-in-progress", 2), ("initiate-transfer", 3), ("initiate-transfer-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpInitiate.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpInitiate.setDescription('This object is used to initiate the TFTP transfers configured in cpqnTftpTable. When setting this object, the only valid values are initiate-transfer(3) and initiate_transfer-reset(4). Attempts to set this object to other values are rejected with a Bad Value error. When this object is set to initiate-transfer(3), the agent does not reset (reboot) after the TFTP transfer(s) is(are) complete. Normal agent operation is resumed after the transfer(s). During the transfer(s), SNMP communication may or may not be available; consult the product-specific documentation. When this object is set to initiate-transfer-reset(4), the agent performs a reset (reboot) after the TFTP transfer(s) is(are) complete. SNMP communication may be lost at some point during the transfer/reset activity. SNMP communication resumes once the agent reset is complete. If the agent does not support the requested transfer mode, it rejects the set request with a Bad Value error. The agent returns transfer-in-progress(2) when this object is queried while a TFTP transfer is in progress. In order to avoid unexpected results, it is invalid to modify set any objects in cpqnTftpTable while this object is set to transfer-in-progress(2). The agent sets this object to no-transfer-ipr(1) after all TFTP transfers are completed.')
cpqnTftpCanDldAfterBoot = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("can-dld-after-boot", 1), ("cannot-dld-after-boot", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpCanDldAfterBoot.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpCanDldAfterBoot.setDescription('The agent returns can-dld-after-boot(1) if it allows cpqnTftpTransferState to be set to download-afterboot(3). The purpose of this object is to inform the management station of the file transfer capabilities of the agent.')
cpqnTftpCanSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("can-send-tftp-trap", 1), ("cannot-send-tftp-trap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpCanSendTrap.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpCanSendTrap.setDescription('The agent returns can-send-tftp-trap(1) if it allows cpqnTftpTrapEnableStatus to be set. If the agent returns cannot-send-tftp-trap(2), then sets on cpqnTftpTrapEnableStatus are rejected with a Bad Value error, and gets always return disabled(2). The purpose of this object is to inform the management station of the trap capabilities of the agent.')
cpqnTftpTrapEnableStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 121, 9, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("os-file-traps", 3), ("cfg-file-traps", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpTrapEnableStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpTrapEnableStatus.setDescription('DURABLE: This object is used to enable TFTP file transfer traps. If the agent does not support these traps, then it return a Bad Value error when this object is set. The cpqnTftpCanSendTrap object indicates whether or not the agent supports traps.')
cpqnTftpTable = MibTable((1, 3, 6, 1, 4, 1, 232, 121, 9, 5), )
if mibBuilder.loadTexts: cpqnTftpTable.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpTable.setDescription('A table containing the possible file types and names that can be downloaded/uploaded to a device.')
cpqnTftpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1), ).setIndexNames((0, "CPQNTFTP-MIB", "cpqnTftpFileType"))
if mibBuilder.loadTexts: cpqnTftpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpEntry.setDescription('A list of the TFTP file types, names, and statuses.')
cpqnTftpFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("entire-file", 1), ("boot", 2), ("run-time", 3), ("sblock-ext", 4), ("config", 5), ("agent", 6), ("fddi-ulfw", 7), ("atm-ulfw", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpFileType.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpFileType.setDescription('The type of download/upload file that this table entry configures. This object is used as an index into cpqnTftpTable. There is only one entry for each type of file. The agent for a specific product may not support all file types; consult the product-specific documentation for information on using this object.')
cpqnTftpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 2), CpqnRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpRowStatus.setDescription("DURABLE: The status of this row entry. Entries are added to this table using 'row sets'. When an entry is added, this object must be set to row-valid(1). To delete an entry from this table, set this object for the entry to row-invalid(2). Row sets for new entries with a row status set to row-invalid(2) return a Bad Value error. Attempts to read invalid entries are rejected with a No Such error. This table is indexed by cpqnTftpFileType. If an attempt is made to set this object for an invalid cpqnTftpFileType value, then a Bad Value error is returned.")
cpqnTftpPathname = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpPathname.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpPathname.setDescription('DURABLE: The fully-qualified path and filename (as recognized by the TFTP server) of the file to download or upload.')
cpqnTftpServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpServerIp.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpServerIp.setDescription('DURABLE: The IP address of the TFTP server.')
cpqnNewFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnNewFileVersion.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnNewFileVersion.setDescription('DURABLE: This object specifies the version of the file to be downloaded. The agent uses this value to validate the downloaded file. An agent may allow this object to be left blank, in which case validation of the file versions will not be done (used for testing images, forcing a file when a version is not known, etc. Refer to the product-specific documentation for details on using this object.')
cpqnTftpTransferState = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-download-ipr", 1), ("download", 2), ("download-afterboot", 3), ("upload-to-nms", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqnTftpTransferState.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpTransferState.setDescription("DURABLE: This object configures this entry's type of TFTP transfer (download/upload) and when it occurs after cpqnTftpInitiate is set appropriately (immediately or after the next restart). Note that multiple cpqnTftpTable entries may enable TFTP transfers; the order in which the entries are processed is left to the agent. After the TFTP transfer has been completed (successfully or not), the agent sets this object back to no-download-ipr(1). If the agent is restarted before the transfer occurs, then this object's value is retained. Support for download-afterboot(3) and upload-to-nms(4) is optional. Attempts to set this object to an unsupported value are rejected with a Bad Value error. The cpqnTftpCanDldAfterBoot object indicates whether or not the agent supports download-afterboot(3). Refer to product-specific documentation for information on upload-to-nms(4).")
cpqnTftpTransferLastErr = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("no-error", 1), ("transfer-in-progress", 2), ("download-failed", 3), ("upload-failed", 4), ("tftp-timeout", 5), ("route-not-found", 6), ("file-not-found", 7), ("invalid-access", 8), ("disk-full", 9), ("illegal-tftp-op", 10), ("unk-xfer-id", 11), ("file-exists", 12), ("no-such-user", 13), ("invalid-version", 14), ("hardware-error", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpTransferLastErr.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpTransferLastErr.setDescription('DURABLE: This is the error status (if any) of the last upload or download that occurred for this entry.')
cpqnTftpErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 121, 9, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqnTftpErrorText.setStatus('mandatory')
if mibBuilder.loadTexts: cpqnTftpErrorText.setDescription('DURABLE: This is a text message from the last TFTP transfer. When possible, the message is obtained directly from the most recent TFTP error packet. If there was not a TFTP error packet, then a suitable message is returned.')
cpqnTftpTransferInitiated = NotificationType((1, 3, 6, 1, 4, 1, 232, 121) + (0,1)).setObjects(("CPQNTFTP-MIB", "cpqnTftpFileType"), ("CPQNTFTP-MIB", "cpqnTftpPathname"), ("CPQNTFTP-MIB", "cpqnTftpTransferState"))
if mibBuilder.loadTexts: cpqnTftpTransferInitiated.setDescription('This trap is sent whenever a SNMP-requested TFTP transaction is initiated, depending on the value of cpqnTftpTrapEnableStatus. For those cases where multiple files are downloaded, multiple traps are sent.')
cpqnTftpTransferCompleted = NotificationType((1, 3, 6, 1, 4, 1, 232, 121) + (0,2)).setObjects(("CPQNTFTP-MIB", "cpqnTftpFileType"), ("CPQNTFTP-MIB", "cpqnTftpPathname"), ("CPQNTFTP-MIB", "cpqnTftpTransferState"), ("CPQNTFTP-MIB", "cpqnTftpTransferLastErr"))
if mibBuilder.loadTexts: cpqnTftpTransferCompleted.setDescription('This trap is sent whenever a SNMP-requested TFTP transaction is completed, depending on the value of cpqnTftpTrapEnableStatus. For those cases where multiple files are downloaded, multiple traps are sent. NOTE: It may not be possible for an agent to send this trap. Support of this trap is optional.')
mibBuilder.exportSymbols("CPQNTFTP-MIB", cpqnTftpTable=cpqnTftpTable, cpqnTftpTransferCompleted=cpqnTftpTransferCompleted, cpqnNewFileVersion=cpqnNewFileVersion, cpqnTftpTrapEnableStatus=cpqnTftpTrapEnableStatus, cpqnTftpTransferLastErr=cpqnTftpTransferLastErr, cpqnTftpEntry=cpqnTftpEntry, cpqnTftpRowStatus=cpqnTftpRowStatus, cpqnTftpCanDldAfterBoot=cpqnTftpCanDldAfterBoot, cpqnTftpErrorText=cpqnTftpErrorText, cpqnTftpInitiate=cpqnTftpInitiate, cpqnTftpTransferState=cpqnTftpTransferState, cpqnTftpServerIp=cpqnTftpServerIp, compaq=compaq, cpqnCommon=cpqnCommon, cpqnTftpCanSendTrap=cpqnTftpCanSendTrap, cpqnTftpConfig=cpqnTftpConfig, cpqnTftpFileType=cpqnTftpFileType, cpqnTftpPathname=cpqnTftpPathname, cpqnTftpTransferInitiated=cpqnTftpTransferInitiated)
