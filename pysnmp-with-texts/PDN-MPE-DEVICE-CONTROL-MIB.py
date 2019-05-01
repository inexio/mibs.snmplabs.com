#
# PySNMP MIB module PDN-MPE-DEVICE-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-DEVICE-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
pdn_mpe, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-mpe")
ResetStates, = mibBuilder.importSymbols("PDN-TC", "ResetStates")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, NotificationType, MibIdentifier, ObjectIdentity, TimeTicks, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Unsigned32, Bits, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "MibIdentifier", "ObjectIdentity", "TimeTicks", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Unsigned32", "Bits", "Integer32", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
mpeDevControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10))
mpeDevControl.setRevisions(('1902-04-29 00:00', '1902-04-09 09:05', '1900-11-21 18:00', '1900-10-26 14:00', '1900-10-18 18:30', '1900-10-06 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mpeDevControl.setRevisionsDescriptions(('Aamir Shaikh o Adding mpeDevControlExtendedSelfTest object', 'Kathy Wilson o Add mpeDevFileXferFileFormat object', 'Delete CCM objects and traps', 'Combine the mpeCCMResync objects', 'Addition of mpeCCMAutoBackupType object', 'Initial conversion to SMIv2',))
if mibBuilder.loadTexts: mpeDevControl.setLastUpdated('0204290000Z')
if mibBuilder.loadTexts: mpeDevControl.setOrganization('Paradyne Corporation MIB Working Group')
if mibBuilder.loadTexts: mpeDevControl.setContactInfo('Paradyne Corporation 8545 126th Avenue North Largo, FL 33733 www.paradyne.com General Comments to: mibwg_team@paradyne.com Editors Prakash Easwar Rajesh Raghaven Kathy Wilson Aamir Shaikh')
if mibBuilder.loadTexts: mpeDevControl.setDescription('This MIB Module allows a user to reset a device in the DSLAM, as well as perform various operations related to the storage and retrieval of firmware and configuration files on devices.')
mpeDevControlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1))
mpeDevControlMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2))
mpeDevControlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3))
mpeDevHwControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1))
mpeDevFileXferConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2))
mpeDevFirmwareControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3))
mpeDevTestControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4))
mpeDevControlMIBTrapsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2, 0))
if mibBuilder.loadTexts: mpeDevControlMIBTrapsV2.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlMIBTrapsV2.setDescription('The traps for the device control MIB.')
mpeDevControlTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1), )
if mibBuilder.loadTexts: mpeDevControlTable.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTable.setDescription('A table that contains generic information about Card Control.')
mpeDevControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevControlEntry.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlEntry.setDescription('A list of information for device Control.')
mpeDevControlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1, 1, 1), ResetStates()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevControlReset.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlReset.setDescription('Writing the value reset (2) to this object initiates a Hardware power-on reset of the device. Writing the value resetToFactoryDefaults (3) causes the device to re-configure itself with factory defaults. Writing the value (4) causes the device to re-configure itself with a previously loaded active configuration. The value read from this object is noOp(1).')
mpeDevControlSelfTestTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2), )
if mibBuilder.loadTexts: mpeDevControlSelfTestTable.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlSelfTestTable.setDescription('A table containing information to control device specific Self-Test operations.')
mpeDevControlSelfTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevControlSelfTestEntry.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlSelfTestEntry.setDescription('A list of objects for performing Self-Test operations.')
mpeDevControlExtendedSelfTest = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("enableExtendSelfTestAndReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeDevControlExtendedSelfTest.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlExtendedSelfTest.setDescription('This object is used to start the extended Power-On Self-Test test. Writing the value enableExtendSelfTestAndReset(2) to this object resets the device and puts it into extended Power-On Self-Test mode. During device initialization, the extended Self-Test would be carried out first and then the device would carry out its normal boot operation. The value read from this object is noOp(1). Writing back the same value, noOp(1) will not start the test. Note that if extended Self-Test fails for some reason, after re-initialization, the value of this object will default to enableExtendSelfTestAndReset(2) again unless the manager explicitly chooses not to do so.')
mpeDevControlTestTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3), )
if mibBuilder.loadTexts: mpeDevControlTestTable.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTestTable.setDescription('A table that contains configuration information to perform device specific tests.')
mpeDevControlTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevControlTestEntry.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTestEntry.setDescription('A list of configuration information for device specific tests.')
mpeDevControlTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("lampTest", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeDevControlTestType.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTestType.setDescription('This object is used to specify the type of the test to start.')
mpeDevControlTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevControlTestStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTestStatus.setDescription('The test status on the device. This object indicates whether the indexed test is currently active(1) or inactive(2).')
mpeDevControlTestCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpeDevControlTestCmd.setStatus('current')
if mibBuilder.loadTexts: mpeDevControlTestCmd.setDescription('Used to start or stop the indexed test. When read, the value returned will be the next logical command.')
mpeDevFileXferConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1), )
if mibBuilder.loadTexts: mpeDevFileXferConfigTable.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferConfigTable.setDescription('The Paradyne FileXfer Client Config Table.')
mpeDevFileXferConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpeDevFileXferConfigEntry.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferConfigEntry.setDescription(' Use of the File Tranfer MIB could be used with other MIBS in the following manner: a) Use another MIB/means to verify available space /make room for a file to be transfered to this device b) Use this MIB to download the file c) Use another MIB/means to select the file you want to make active if your selecting firmware for example. d) Use another MIB/means to reset the device. A management station wishing to initiate a file transfer needs to create an entry in this table. To do so, you must first identify the entPhysicalIndex of the device you intend to do the transfer with. You should then create the associated instance of the row status It must also, either in the same or in successive PDUs, create an instance of mpeDevFileXferFileName, mpeDevFileXferFileType, . mpeDevFileXferServerIpAddress, mpeDevFileXferOperation. It should also modify the default values for the other configuration objects if the defaults are not appropriate. Once the appropriate instance of all the configuration objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the request. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non-defaulted configuration objects. Once the MpeDevFileXferConfigEntry request has been created (i.e. the mpeDevFileXferRowStatus has been made active), the entry cannot be modified - the only operation possible after this is to delete the row. Once the request completes, the management station should retrieve the values of the status objects of interest, and should then delete the entry. In order to prevent old entries from clogging the table, entries could be aged out, but an entry will never be deleted within 5 minutes of completing. ')
mpeDevFileXferFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferFileName.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferFileName.setDescription('This object contains the name of the filetransfer file.')
mpeDevFileXferCopyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tftp", 1), ("ftp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferCopyProtocol.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferCopyProtocol.setDescription('The transfer protocol that should be used to copy the file across the network. If the file transfer is to occur locally on the SNMP agent, the method of transfer is left upto the implementation, and is not restricted to the protocols below.')
mpeDevFileXferFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("firmware", 1), ("config", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferFileType.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferFileType.setDescription('Specifies the type of file your want to transfer.')
mpeDevFileXferServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferServerIpAddress.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferServerIpAddress.setDescription("This object contains the file transfer server's IP address. ")
mpeDevFileXferUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferUserName.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferUserName.setDescription('This object contains the username if a username is needed to login to the server.')
mpeDevFileXferUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferUserPassword.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferUserPassword.setDescription('This object contains the password if a password is needed to login to the server. This object will return null on a read operation.')
mpeDevFileXferOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("get", 1), ("put", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferOperation.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferOperation.setDescription('This object contains the operation the file transfer wants to perform.')
mpeDevFileXferPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferPktsSent.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferPktsSent.setDescription('This object contains the the number of packets sent to the server at the time of interrogation.')
mpeDevFileXferPktsRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferPktsRecv.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferPktsRecv.setDescription('This object contains the the number of packets received from the server at the time of interrogation.')
mpeDevFileXferOctetsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferOctetsSent.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferOctetsSent.setDescription('This object contains the the number of octets sent to the server at the time of interrogation.')
mpeDevFileXferOctetsRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferOctetsRecv.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferOctetsRecv.setDescription('This object contains the the number of octets received from the server at the time of interrogation.')
mpeDevFileXferOwnerString = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferOwnerString.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferOwnerString.setDescription("The entity which currently has the 'ownership' required to invoke the operation on this index.")
mpeDevFileXferStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("failure", 3), ("inprogress", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferStatus.setDescription('This object contains the status of the file transfer.')
mpeDevFileXferErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferErrorStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferErrorStatus.setDescription('This object contains the reason code of the failure determined in mpeDevFileXferStatus. The reason code are specific to the file transfer protocol. Please refer to the file transfer protocols respective RFC for clarification of the error code value meanings. TFTP Error Codes from rfc 1350 FTP Error Codes from rfc 959')
mpeDevFileXferSendEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferSendEvent.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferSendEvent.setDescription('This object indicates whether or not to send the mpeDevFileXferEvent event trap .')
mpeDevFileXferRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferRowStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferRowStatus.setDescription('This object is used to create a new row or delete an existing row in this table.')
mpeDevFileXferXferTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFileXferXferTime.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferXferTime.setDescription('This object indicates the elapsed time (in hundredths of a second) of the file transfer.')
mpeDevFileXferFileFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascii", 1), ("binary", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFileXferFileFormat.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferFileFormat.setDescription('This object contains the file representation type. A file representation type of ascii implies an ASCII, non-print text file. A file representation type of binary implies an binary image file. The default file representation type is binary(2).')
mpeDevFirmwareControlTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1), )
if mibBuilder.loadTexts: mpeDevFirmwareControlTable.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlTable.setDescription('A list of the current Firmware Releases and their associated status. Each Firmware Release will be indexed by a number from 1 to N. The user will be able to view the Firmware Release String and Operational Status of the release (valid or invalid) and activate a valid Firmware Release by changing the Administration Status to active.')
mpeDevFirmwareControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlIndex"))
if mibBuilder.loadTexts: mpeDevFirmwareControlEntry.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlEntry.setDescription('The Device Firmware Release entry.')
mpeDevFirmwareControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFirmwareControlIndex.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlIndex.setDescription('This object is used to index the Firmware table (range 1 to N).')
mpeDevFirmwareControlRelease = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFirmwareControlRelease.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlRelease.setDescription('This object indicates the Software Release for this Firmware. If the Software Firmware is Operational Status is invalid, the Software Revision Number will be blank.')
mpeDevFirmwareControlOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpeDevFirmwareControlOperStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlOperStatus.setDescription('This object indicates whether or not the indexed Firmware entry contains a valid(1) or invalid(2) Firmware.')
mpeDevFirmwareControlAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mpeDevFirmwareControlAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlAdminStatus.setDescription('This object indicates whether or not the indexed Firmware entry is active(1) or inactive(2). Writing active(1) will activate that software release and cause the unit to reset (response may timeout). Writing active(1) to a Firmware entry whose mpeDevFirmwareControlOperStatus is invalid will return BAD VALUE. Writing inactive(2) will always return BAD VALUE.')
mpeDevFileXferEvent = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2, 0, 1)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferErrorStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOperation"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileType"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileName"))
if mibBuilder.loadTexts: mpeDevFileXferEvent.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferEvent.setDescription('This trap is to communicate a couple of things about the completion of a file transfer. mpeDevFileXferStatus - Did it complete successfully or not. mpeDevFileXferErrorStatus - If not, what was the error code. mpeDevFileXferOperation - What operation was performed?. mpeDevFileXferFileType - Was it a firmware xfer or config? mpeDevFileXferFileName - The name of the file transfered. ')
mpeDevHwControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 1)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlReset"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlExtendedSelfTest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDevHwControlGroup = mpeDevHwControlGroup.setStatus('current')
if mibBuilder.loadTexts: mpeDevHwControlGroup.setDescription('Objects necessary to implement minimal hardware control')
mpeDevFileXferConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 2)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileName"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferCopyProtocol"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileType"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferServerIpAddress"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferUserName"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferUserPassword"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOperation"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferPktsSent"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferPktsRecv"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOctetsSent"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOctetsRecv"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOwnerString"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferErrorStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferSendEvent"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferRowStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferXferTime"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileFormat"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDevFileXferConfigGroup = mpeDevFileXferConfigGroup.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferConfigGroup.setDescription('Object group used to implement file transfer functionality')
mpeDevFirmwareControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 3)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlIndex"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlRelease"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlOperStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDevFirmwareControlGroup = mpeDevFirmwareControlGroup.setStatus('current')
if mibBuilder.loadTexts: mpeDevFirmwareControlGroup.setDescription('Object group used to manage firmware releases on devices')
mpeDevTestControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 4)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestType"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestStatus"), ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestCmd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDevTestControlGroup = mpeDevTestControlGroup.setStatus('current')
if mibBuilder.loadTexts: mpeDevTestControlGroup.setDescription('Objects necessary to implement device specific tests')
mpeDevFileXferEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 5)).setObjects(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mpeDevFileXferEventGroup = mpeDevFileXferEventGroup.setStatus('current')
if mibBuilder.loadTexts: mpeDevFileXferEventGroup.setDescription('Notifications associated with mpeDevFileXferConfigGroup')
mibBuilder.exportSymbols("PDN-MPE-DEVICE-CONTROL-MIB", mpeDevControlReset=mpeDevControlReset, mpeDevControl=mpeDevControl, mpeDevFileXferConfigTable=mpeDevFileXferConfigTable, mpeDevFirmwareControlTable=mpeDevFirmwareControlTable, mpeDevControlTestCmd=mpeDevControlTestCmd, mpeDevFileXferFileType=mpeDevFileXferFileType, mpeDevFileXferOctetsSent=mpeDevFileXferOctetsSent, mpeDevFileXferUserPassword=mpeDevFileXferUserPassword, mpeDevControlMIBObjects=mpeDevControlMIBObjects, mpeDevControlSelfTestTable=mpeDevControlSelfTestTable, mpeDevFileXferOwnerString=mpeDevFileXferOwnerString, mpeDevFileXferFileFormat=mpeDevFileXferFileFormat, mpeDevFirmwareControlAdminStatus=mpeDevFirmwareControlAdminStatus, mpeDevFileXferOctetsRecv=mpeDevFileXferOctetsRecv, mpeDevControlTestEntry=mpeDevControlTestEntry, mpeDevFirmwareControlIndex=mpeDevFirmwareControlIndex, mpeDevFileXferPktsRecv=mpeDevFileXferPktsRecv, mpeDevFileXferRowStatus=mpeDevFileXferRowStatus, mpeDevControlMIBTrapsV2=mpeDevControlMIBTrapsV2, mpeDevFileXferOperation=mpeDevFileXferOperation, mpeDevFileXferConfig=mpeDevFileXferConfig, mpeDevFileXferErrorStatus=mpeDevFileXferErrorStatus, mpeDevControlEntry=mpeDevControlEntry, mpeDevFileXferEvent=mpeDevFileXferEvent, mpeDevFileXferCopyProtocol=mpeDevFileXferCopyProtocol, mpeDevFirmwareControlEntry=mpeDevFirmwareControlEntry, mpeDevFirmwareControlRelease=mpeDevFirmwareControlRelease, mpeDevFileXferSendEvent=mpeDevFileXferSendEvent, mpeDevFileXferXferTime=mpeDevFileXferXferTime, mpeDevFirmwareControlGroup=mpeDevFirmwareControlGroup, mpeDevFileXferServerIpAddress=mpeDevFileXferServerIpAddress, mpeDevFileXferEventGroup=mpeDevFileXferEventGroup, mpeDevControlTestTable=mpeDevControlTestTable, mpeDevControlTestType=mpeDevControlTestType, mpeDevFileXferFileName=mpeDevFileXferFileName, mpeDevFileXferConfigGroup=mpeDevFileXferConfigGroup, mpeDevControlTestStatus=mpeDevControlTestStatus, PYSNMP_MODULE_ID=mpeDevControl, mpeDevFileXferStatus=mpeDevFileXferStatus, mpeDevControlSelfTestEntry=mpeDevControlSelfTestEntry, mpeDevFirmwareControlOperStatus=mpeDevFirmwareControlOperStatus, mpeDevHwControlGroup=mpeDevHwControlGroup, mpeDevHwControl=mpeDevHwControl, mpeDevTestControlGroup=mpeDevTestControlGroup, mpeDevControlMIBGroups=mpeDevControlMIBGroups, mpeDevTestControl=mpeDevTestControl, mpeDevFileXferConfigEntry=mpeDevFileXferConfigEntry, mpeDevControlExtendedSelfTest=mpeDevControlExtendedSelfTest, mpeDevFirmwareControl=mpeDevFirmwareControl, mpeDevFileXferUserName=mpeDevFileXferUserName, mpeDevFileXferPktsSent=mpeDevFileXferPktsSent, mpeDevControlTable=mpeDevControlTable, mpeDevControlMIBTraps=mpeDevControlMIBTraps)
