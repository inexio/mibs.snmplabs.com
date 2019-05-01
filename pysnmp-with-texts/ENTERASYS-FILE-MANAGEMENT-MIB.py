#
# PySNMP MIB module ENTERASYS-FILE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-FILE-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
hrFSIndex, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "hrFSIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, iso, TimeTicks, Bits, MibIdentifier, IpAddress, ObjectIdentity, Unsigned32, Counter64, ModuleIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "iso", "TimeTicks", "Bits", "MibIdentifier", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter64", "ModuleIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString, StorageType, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "StorageType", "RowStatus", "DateAndTime")
etsysFileManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15))
etsysFileManagementMIB.setRevisions(('2001-12-03 19:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysFileManagementMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysFileManagementMIB.setLastUpdated('200112031954Z')
if mibBuilder.loadTexts: etsysFileManagementMIB.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: etsysFileManagementMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 Phone: +1 603 332 9400 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysFileManagementMIB.setDescription('This MIB module defines a portion of the SNMP enterprise MIBs under the Enterasys enterprise OID pertaining to the transferring and management of files for Enterasys products.')
etsysFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1))
etsysFileListing = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2))
etsysFileOperation = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3))
etsysFileConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4))
etsysFileTransferRequestLimit = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestLimit.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestLimit.setDescription('The maximum number of file transfer requests this entity can hold in the etsysFileTransferRequestTable. A value of 0 indicates no configured limit.')
etsysFileTransferRequestsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestsCurrent.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestsCurrent.setDescription('The number of file transfer requests currently in the etsysFileTransferRequestTable.')
etsysFileTransferRequestsCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestsCompleted.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestsCompleted.setDescription('The number of file transfer requests that have completed successfully or otherwise. This object SHOULD be stored in persistent memory.')
etsysFileTransferRequestSupportedURLs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 4), Bits().clone(namedValues=NamedValues(("etsysFileTransferFtp", 0), ("etsysFileTransferRcp", 1), ("etsysFileTransferHttp", 2), ("etsysFileTransferTftp", 3), ("etsysFileTransferFile", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestSupportedURLs.setReference('RFC 1738 - Uniform Resource Locators (URL), RFC 2396 - Uniform Resource Identifiers (URI): Generic Syntax')
if mibBuilder.loadTexts: etsysFileTransferRequestSupportedURLs.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestSupportedURLs.setDescription('The URLs that this entity supports for transferring files. These define the transfer protocols and local file types. In the case that any URL is supported only as a source or destination file then an appropriate SNMP set failure should occur when attempting to use that URL in an unsupported manner. etsysFileTransferFtp - As per rfc1738 ftp://<user>:<password>@<host>:<port>/<url-path> url-path: <cwd1>/<cwd2>/.../<cwdN>/<name>;type=<typecode> user defaults to anonymous, password to snmp@<domain-name>, port to 21, and type to ASCII. binary and image are both valid types which have the same meaning. domain-name would be the IP address or domain name of the managed entity. etsysFileTransferRcp - rcp://<user>@<host>:<port>/<cwd1>/<cwd2>/.../<cwdN>/<name> port defaults to 514. etsysFileTransferHttp - As per rfc1738 http://<host>:<port>/<path>?<searchpart> port defaults to 80. etsysFileTransferTftp - tftp://<host>:<port>/<cwd1>/<cwd2>/.../<cwdN>/<name> port defaults to 69. etsysFileTransferFile - As per rfc1738 file://<host>/<path> host can only be specified as localhost or the empty string. This will only be used to specify a file on the managed entity. This indicates that the managed entity supports some form of a file system.')
etsysFileTransferRequestNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestNextAvailableIndex.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestNextAvailableIndex.setDescription('This object indicates the numerically lowest available index within this entity, which may be used for the value of etsysFileTransferRequestIndex in the creation of a new entry in the etsysFileTransferRequestTable. An index is considered available if the index value falls within the range of 1 to etsysFileTransferRequestLimit and is not being used to index an existing entry in the etsysFileTransferRequestTable contained within this entity. A value of zero indicates that all of the entries in the etsysFileTransferRequestTable are currently in use. This value should only be considered a guideline for management creation of etsysFileTransferRequestTable entries, there is no requirement on management to create entries based upon this index value.')
etsysFileTransferRequestTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6), )
if mibBuilder.loadTexts: etsysFileTransferRequestTable.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestTable.setDescription('A table of file transfer requests.')
etsysFileTransferRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1), ).setIndexNames((0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestIndex"))
if mibBuilder.loadTexts: etsysFileTransferRequestEntry.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestEntry.setDescription('An entry describing a particular file transfer request.')
etsysFileTransferRequestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysFileTransferRequestIndex.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestIndex.setDescription('An arbitrary index for this file transfer request.')
etsysFileTransferRequestSource = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileTransferRequestSource.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestSource.setDescription('URL of the source file. Any password information MUST NOT be returned on a read. If a managed entity supports some form of a file system and the file URL from rfc1738 then a file copy can be performed by using the file URL for both the source and destination. Activating the row with the URL specifying the same file in the source and destination SHOULD cause the file transfer to fail.')
etsysFileTransferRequestDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileTransferRequestDestination.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestDestination.setDescription('URL of the destination file. Any password information MUST NOT be returned on a read. Two transfer request entries SHOULD NOT be allowed to specify the same destination URL. To initiate a second transfer to the same destination URL the original entry must be reused or destroyed. Any errors with the type or format of these URLs SHOULD be reported in the etsysFileTransferRequestErrorDescription object when the row is activated.')
etsysFileTransferRequestOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("pending", 2), ("running", 3), ("success", 4), ("failure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestOperStatus.setDescription("The operational state of the file transfer. inactive - Indicates that the RowStatus of this conceptual row is not in the 'active' state. pending - Indicates that the transfer described by this row is ready to run and waiting in a queue. running - Indicates that the transfer described by this row is running. success - Indicates that the transfer described by this row has successfully run to completion. failure - Indicates that the transfer described by this row has failed to run to completion.")
etsysFileTransferRequestEnqueuedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 5), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestEnqueuedTime.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestEnqueuedTime.setDescription("The date and time, in device local time, when this transfer request was last enqueued for execution. The value '0000000000000000'H is returned if this table entry has not yet been queued.")
etsysFileTransferRequestCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 6), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestCompletionTime.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestCompletionTime.setDescription("The date and time, in device local time, when this transfer request was last completed. It SHOULD be reset to the default value when the RowStatus of this conceptual row is set to active. The value '0000000000000000'H is returned if this table entry has not yet run to completion.")
etsysFileTransferRequestBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestBytesTransferred.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestBytesTransferred.setDescription('The number of bytes currently transferred. A value of -1 indicates that this feature is not supported for the protocol currently selected. This value is reset to its initial state when the etsysFileTransferRequestRowStatus object is set to the active state.')
etsysFileTransferRequestErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 8), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestErrorDescription.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestErrorDescription.setDescription('This object contains a descriptive error message if the requested transfer failed. Implementations must reset the error message to a zero-length string when the etsysFileTransferRequestRowStatus leaf is set to the active state.')
etsysFileTransferRequestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 9), StorageType().clone('volatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileTransferRequestStorageType.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestStorageType.setDescription('Allows applications within the managed entity to define nonVolatile or readOnly rows as required.')
etsysFileTransferRequestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileTransferRequestRowStatus.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferRequestRowStatus.setDescription("A control that allows entries to be added, activated, deactivated, and removed from this table. When the value of this object is 'active' none of the other objects in this conceptual row can be modified. Setting this object to the 'active' state from the 'notInService' state will cause the requested file transfer to be initiated or queued. Once the requested file transfer has completed, successfully or otherwise, this leaf will be set to the 'notInService' state by the managed entity. Setting this object to any other valid state from the 'active' state will interrupt the file transfer request. Setting this object to the 'active' state from the 'active' state will not have any affect. Conceptual rows that have been in the 'notInService' state for more than a device specific time period MAY be destroyed by the managed entity.")
etsysFileListingTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1), )
if mibBuilder.loadTexts: etsysFileListingTable.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingTable.setDescription('A table of user files currently stored in a particular file system on this entity. If the Host Resources MIB is not supported and there is only one file system use the value of one for the hrFSIndex. This table should represent a minimal set of information that is commonly available on most file systems.')
etsysFileListingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1), ).setIndexNames((0, "HOST-RESOURCES-MIB", "hrFSIndex"), (0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingIndex"))
if mibBuilder.loadTexts: etsysFileListingEntry.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingEntry.setDescription('An entry describing a particular file currently stored on this entity.')
etsysFileListingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysFileListingIndex.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingIndex.setDescription('The locally arbitrary, but unique identifier associated with this file entry.')
etsysFileListingFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileListingFileName.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingFileName.setDescription('The fully qualified name of the file.')
etsysFileListingFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileListingFileSize.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingFileSize.setDescription('The size in bytes of this file.')
etsysFileListingFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unsupported", 1), ("directory", 2), ("ordinary-file", 3), ("symbolic-link", 4))).clone('unsupported')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileListingFileType.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingFileType.setDescription('The type of file that this entry represents.')
etsysFileListingFileDate = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 5), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileListingFileDate.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingFileDate.setDescription("The time and date that this file was last modified, if this information is unavailable return '0000000000000000'H.")
etsysFileListingFileOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 6), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileListingFileOrigin.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingFileOrigin.setDescription('The source URL of this file, if it was created by a transfer, or an application name, if it was created by an application. If this information is unavailable return the null string. Since most of the user files on our devices are, or would be, created by file transfers or applications this would be an interesting but otherwise uncommon piece of information.')
etsysFileOperationLimit = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileOperationLimit.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationLimit.setDescription('The maximum number of requests this entity can hold in the etsysFileOperationTable. A value of 0 indicates no configured limit.')
etsysFileOperationsCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileOperationsCurrent.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationsCurrent.setDescription('The number of requests currently in the etsysFileOperationTable.')
etsysFileOperationsCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileOperationsCompleted.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationsCompleted.setDescription('The number of file operations that have completed successfully or otherwise. This object SHOULD be stored in persistent memory.')
etsysFileOperationNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileOperationNextAvailableIndex.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationNextAvailableIndex.setDescription('This object indicates the numerically lowest available index within this entity, which may be used for the value of etsysFileOperationIndex in the creation of a new entry in the etsysFileOperationTable. An index is considered available if the index value falls within the range of 1 to etsysFileOperationLimit and is not being used to index an existing entry in the etsysFileOperationTable contained within this entity. A value of zero indicates that all of the entries in the etsysFileOperationTable are currently in use. This value should only be considered a guideline for management creation of etsysFileOperationTable, there is no requirement on management to create entries based upon this index value.')
etsysFileOperationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5), )
if mibBuilder.loadTexts: etsysFileOperationTable.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationTable.setDescription('Entries can be created in this table to rename and delete files on this entity.')
etsysFileOperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1), ).setIndexNames((0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationIndex"))
if mibBuilder.loadTexts: etsysFileOperationEntry.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationEntry.setDescription('An entry describing an operation to be performed on the named file on this entity.')
etsysFileOperationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: etsysFileOperationIndex.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationIndex.setDescription('The locally arbitrary, but unique identifier associated with this file operation entry.')
etsysFileOperationType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("delete", 1), ("rename", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileOperationType.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationType.setDescription('The operation that should be performed on the named file.')
etsysFileOperationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 3), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileOperationFileName.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationFileName.setDescription('The fully qualified name of the file that this operation will be applied to.')
etsysFileOperationFileNewName = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 4), SnmpAdminString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileOperationFileNewName.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationFileNewName.setDescription('The new fully qualified name for this file. This object is only required for the rename operation type.')
etsysFileOperationErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 5), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysFileOperationErrorDescription.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationErrorDescription.setDescription('This object contains a descriptive error message if the requested operation failed. Implementations must reset the error message to a zero-length string when the etsysFileOperationRowStatus leaf is set to the active state.')
etsysFileOperationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysFileOperationRowStatus.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationRowStatus.setDescription("A control that allows entries to be added, activated, deactivated, and removed from this table. When the value of this object is 'active' none of the other objects in this conceptual row can be modified. Setting this object to the 'active' state from the 'notInService' state will cause the requested file operation to be initiated or queued. Once the requested file operation has completed, successfully or otherwise, this leaf will be set to the 'notInService' state by the managed entity. Setting this object to any other valid state from the 'active' state will cancel the file operation if it has not been started. Setting this object to the 'active' state from the 'active' state will not have any affect. Conceptual rows that have been in the 'notInService' state for some entity specific time period will be destroyed by the managed entity.")
etsysFileGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1))
etsysFileCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 2))
etsysFileTransferGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 1)).setObjects(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestLimit"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestsCurrent"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestsCompleted"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestSupportedURLs"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestNextAvailableIndex"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestSource"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestDestination"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestOperStatus"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestEnqueuedTime"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestCompletionTime"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestBytesTransferred"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestErrorDescription"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestStorageType"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysFileTransferGroup = etsysFileTransferGroup.setStatus('current')
if mibBuilder.loadTexts: etsysFileTransferGroup.setDescription('A group of objects that provide a means to copy and transfer files.')
etsysFileListingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 2)).setObjects(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileName"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileSize"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileType"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileDate"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileOrigin"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysFileListingGroup = etsysFileListingGroup.setStatus('current')
if mibBuilder.loadTexts: etsysFileListingGroup.setDescription('A group of objects that provide a means to list existing files.')
etsysFileOperationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 3)).setObjects(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationLimit"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationsCurrent"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationsCompleted"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationNextAvailableIndex"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationType"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationFileName"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationFileNewName"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationErrorDescription"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysFileOperationGroup = etsysFileOperationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysFileOperationGroup.setDescription('A group of objects that provide a means to rename and delete existing files.')
etsysFileCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 2, 1)).setObjects(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferGroup"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingGroup"), ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysFileCompliance = etsysFileCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysFileCompliance.setDescription('The compliance statement for entities which implement the Enterasys File Management MIB. Implementation of this MIB is based on individual product needs.')
mibBuilder.exportSymbols("ENTERASYS-FILE-MANAGEMENT-MIB", etsysFileOperationFileName=etsysFileOperationFileName, etsysFileTransfer=etsysFileTransfer, etsysFileTransferRequestEntry=etsysFileTransferRequestEntry, etsysFileOperationLimit=etsysFileOperationLimit, etsysFileListingFileDate=etsysFileListingFileDate, etsysFileOperationsCurrent=etsysFileOperationsCurrent, etsysFileGroups=etsysFileGroups, etsysFileListingEntry=etsysFileListingEntry, etsysFileTransferRequestEnqueuedTime=etsysFileTransferRequestEnqueuedTime, etsysFileTransferRequestErrorDescription=etsysFileTransferRequestErrorDescription, etsysFileOperationGroup=etsysFileOperationGroup, etsysFileOperationIndex=etsysFileOperationIndex, etsysFileOperationNextAvailableIndex=etsysFileOperationNextAvailableIndex, PYSNMP_MODULE_ID=etsysFileManagementMIB, etsysFileOperationType=etsysFileOperationType, etsysFileListingFileType=etsysFileListingFileType, etsysFileListingFileName=etsysFileListingFileName, etsysFileTransferRequestsCurrent=etsysFileTransferRequestsCurrent, etsysFileTransferGroup=etsysFileTransferGroup, etsysFileTransferRequestCompletionTime=etsysFileTransferRequestCompletionTime, etsysFileTransferRequestBytesTransferred=etsysFileTransferRequestBytesTransferred, etsysFileListing=etsysFileListing, etsysFileTransferRequestDestination=etsysFileTransferRequestDestination, etsysFileTransferRequestSupportedURLs=etsysFileTransferRequestSupportedURLs, etsysFileTransferRequestStorageType=etsysFileTransferRequestStorageType, etsysFileCompliance=etsysFileCompliance, etsysFileTransferRequestSource=etsysFileTransferRequestSource, etsysFileConformance=etsysFileConformance, etsysFileOperationErrorDescription=etsysFileOperationErrorDescription, etsysFileOperationsCompleted=etsysFileOperationsCompleted, etsysFileTransferRequestLimit=etsysFileTransferRequestLimit, etsysFileOperation=etsysFileOperation, etsysFileTransferRequestRowStatus=etsysFileTransferRequestRowStatus, etsysFileListingGroup=etsysFileListingGroup, etsysFileCompliances=etsysFileCompliances, etsysFileListingIndex=etsysFileListingIndex, etsysFileTransferRequestIndex=etsysFileTransferRequestIndex, etsysFileTransferRequestNextAvailableIndex=etsysFileTransferRequestNextAvailableIndex, etsysFileManagementMIB=etsysFileManagementMIB, etsysFileOperationTable=etsysFileOperationTable, etsysFileOperationEntry=etsysFileOperationEntry, etsysFileTransferRequestsCompleted=etsysFileTransferRequestsCompleted, etsysFileTransferRequestTable=etsysFileTransferRequestTable, etsysFileOperationRowStatus=etsysFileOperationRowStatus, etsysFileOperationFileNewName=etsysFileOperationFileNewName, etsysFileListingFileSize=etsysFileListingFileSize, etsysFileTransferRequestOperStatus=etsysFileTransferRequestOperStatus, etsysFileListingTable=etsysFileListingTable, etsysFileListingFileOrigin=etsysFileListingFileOrigin)
