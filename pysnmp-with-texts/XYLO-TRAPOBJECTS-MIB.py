#
# PySNMP MIB module XYLO-TRAPOBJECTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLO-TRAPOBJECTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:46:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, iso, NotificationType, Integer32, IpAddress, ModuleIdentity, MibIdentifier, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "iso", "NotificationType", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Unsigned32", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
anxTrapHostInfo, modemTrapObj, wanTrapObj, callmgmtTrapObj, genericTrapObj = mibBuilder.importSymbols("XYLO-MIB-SMI", "anxTrapHostInfo", "modemTrapObj", "wanTrapObj", "callmgmtTrapObj", "genericTrapObj")
wanBpvThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanBpvThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanBpvThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanBpvThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter bpv_threshold.')
wanOofThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanOofThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanOofThreshold.setDescription('The threshold which, when met of exceeded, triggers the wanOofThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter oof_threshold.')
wanEsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanEsThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanEsThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanEsThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter es_threshold.')
wanCvThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanCvThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanCvThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanCvThreshtrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter cv_threshold.')
wanEsfThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanEsfThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanEsfThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanEsfThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter esf_threshold.')
wanSesThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanSesThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanSesThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanSesThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter ses_threshold.')
wanUasThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanUasThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanUasThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanUasThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter uas_threshold.')
wanBesThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanBesThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanBesThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanBesThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter bes_threshold.')
wanLofcThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanLofcThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanLofcThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanLofcThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter lofc_threshold.')
wanCssThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wanCssThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wanCssThreshold.setDescription('The threshold which, when met or exceeded, triggers the wanCssThreshTrap to be sent. Setting this object to zero (0) disables the trap. This object corresponds to NA/admin parameter css_threshold.')
ds0ErrorThreshold = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds0ErrorThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: ds0ErrorThreshold.setDescription('This object defines the threshold for the number of consecutive calls that the ds0 fails to accept after which the ds0ErrorTrap is sent to the trap host(s). Setting this object to zero (0) disables the trap This object corresponds to the na/admin parameter ds0_error_threshold.')
mdmErrorTrapThresh = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmErrorTrapThresh.setStatus('mandatory')
if mibBuilder.loadTexts: mdmErrorTrapThresh.setDescription('This object defines the threshold for number of consecutive calls that the modem fails to accept after which the modem is busied out and wanMdmErrorThreshTrap is sent to the trap host(s). Setting this object to zero, disables the trap. Default is zero (disable). This object corresponds to modem_error_threshold NA/admin parameter.')
callBeginTrapObj = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callBeginTrapObj.setStatus('mandatory')
if mibBuilder.loadTexts: callBeginTrapObj.setDescription('This object controls the callBeginTrap trap generation by the RAC. Setting this object to disable, the RAC will not generate the callBeginTrap trap. Default is disable(2). This object corresponds to call_begin_trap NA/admin parameter.')
callEndTrapThresh = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callEndTrapThresh.setStatus('mandatory')
if mibBuilder.loadTexts: callEndTrapThresh.setDescription('This object controls the callEndTrap trap generation by the RAC. Setting this object to zero (default) will disable the trap generation. Setting this object to a value other than zero, the RAC will generate the callEndTrap after than many calls has terminated. A call that has failed to connect is considered a terminated call with appropriate disconnect reason. This object can be used by the manager entity to retrieve the terminated call information from the call history MIB table. Default value is zero. This object corresponds to call_end_trap_inc NA/admin parameter.')
unexpectDisconnectTrapThresh = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unexpectDisconnectTrapThresh.setStatus('mandatory')
if mibBuilder.loadTexts: unexpectDisconnectTrapThresh.setDescription('This object controls the unexpectDisconnectTrap trap generation by the RAC. Setting this object to zero (default) will disable the trap generation. Setting this object to a value other than zero, the RAC will generate the unexpectDisconnectTrap after that many calls has terminated unexpectedly. A call is considered to have disconnected unexpectedly is the call disconnect reason is: protocolError, localHangup, timeoutHDLC, maxLogonTimeout OR if the call is handled by a modem and the modem disconnect reason is : poorSignalQ, failRetrain. This object corresponds to unexpected_trap_inc NA/admin parameter.')
forcedCallDisconnectTrapThresh = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: forcedCallDisconnectTrapThresh.setStatus('mandatory')
if mibBuilder.loadTexts: forcedCallDisconnectTrapThresh.setDescription('This object controls the forcedCallDisconnectTrap trap generation by the RAC. Setting this object to zero (default) will disable the trap generation. Setting this object to a value other than zero, the RAC will generate the forcedCallDisconnectTrap after that many calls has terminated due to timeouts. The RAC has the following timers and setting off either of these timers will generate the trap. The timers are: cliInactivityTimeout - the amount of time in minutes that the RAC (system) waits before hanging up the call. This is valid if the session is in CLI mode. Not applicable for any other sessions (PPP etc). The value of the timer is determined by the object, gpTimerCliInactivity. inactivityTimeout - the amount of time in minutes that the RAC waits before hanging up the call. The timer is independent of the mode of the session. The value of the timer is determined by the object, gpTimerInactivityTimer. netInactivityTimeout - this is similar to the inactivity timeout. This object corresponds to forced_call_inc NA/admin parameter.')
diallnkTrpEna = MibScalar((1, 3, 6, 1, 4, 1, 15, 100, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: diallnkTrpEna.setStatus('mandatory')
if mibBuilder.loadTexts: diallnkTrpEna.setDescription('When enabled, SNMP link up/down traps are generated for remote dialin interfaces.')
anxTrapHostMax = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapHostMax.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostMax.setDescription('The maximum number of rows in the trap host table.')
anxTrapHostCurEnt = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapHostCurEnt.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostCurEnt.setDescription('The current number of rows in the trap host table.')
anxTrapHostNext = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapHostNext.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostNext.setDescription('The index of the next available row to be created in the trap host table. A value of zero means that the table is full and no more rows can be added.')
anxTrapHostTable = MibTable((1, 3, 6, 1, 4, 1, 15, 2, 10, 4), )
if mibBuilder.loadTexts: anxTrapHostTable.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostTable.setDescription('A table of managers which to send traps.')
anxTrapHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1), ).setIndexNames((0, "XYLO-TRAPOBJECTS-MIB", "anxTrapHostIndex"))
if mibBuilder.loadTexts: anxTrapHostEntry.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostEntry.setDescription('A row in the trap host table. The column anxTrapHostStatus is used to create and delete rows in the table. Creation requires a SET PDU with objects anxTrapHostStatus, anxTrapHostAddrType, anxTrapHostNetAddr, and anxTrapHostCommunity for the new row.')
anxTrapHostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapHostIndex.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostIndex.setDescription('The index of the row in the table.')
anxTrapHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("ignore", 3), ("delete", 4), ("create", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostStatus.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostStatus.setDescription("This object is used to create and delete rows in the table and control if they are used. The values that can be written are: valid(2)....if the current status is ignore(3), re-enable this entry for sending traps again ignore(3)...don't use this entry to send traps at this time delete(4)...deletes the row create(5)...creates a new row If the row exists, then a SET with value of create(5) returns error 'badValue'. Deleted rows go away immediately. The following values can be returned on reads: other(1)....some other case valid(2)....the row exists and is valid ignore(3)...don't use this entry to send traps at this time")
anxTrapHostAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ip", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostAddrType.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostAddrType.setDescription('The type of address that is stored in the object anxTrapHostNetAddr. The value is: ip(1)...IP address')
anxTrapHostNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostNetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostNetAddr.setDescription('The network address (in network order) for SNMP manager that is to receive the trap.')
anxTrapHostComm = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostComm.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostComm.setDescription('The community string to use when sending a trap to this host.')
anxTrapHostAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostAgeTime.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostAgeTime.setDescription('The time interval in seconds used to age entries out of the trap receiver table. The default value if not specified will be 0, or infinite,never to be aged out.')
anxTrapHostPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostPortNumber.setDescription('The port number to send the trap to. If this is not enetered the port will default to 162')
anxTrapHostGrouping = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 10, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: anxTrapHostGrouping.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapHostGrouping.setDescription('A bitmask that will associate the trp host entry with one or more trap groupings: none 0x00000000 startup 0x00000001 connection 0x00000002 wan 0x00000004 call-accounting 0x00000008 ospf 0x00000010 all 0xffffffff')
anxTrapUserName = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapUserName.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapUserName.setDescription('A string defining the user name under attack.')
anxTrapPortIndex = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapPortIndex.setDescription('A unique number from 1 to totalPorts that identifies the port under attack.')
anxTrapPortType = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("async", 1), ("sync", 2), ("virtual", 3), ("dialout", 4), ("ethernet", 5), ("rfc", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapPortType.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapPortType.setDescription('A enumerated string that identifies the port type under attack.')
anxTrapInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapInetAddr.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapInetAddr.setDescription('The Internet address of the Annex.')
anxTrapAttackErrcode = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("maxThreshold", 1), ("timeThreshold", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapAttackErrcode.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapAttackErrcode.setDescription('Error code indicating the threshold reached under following circumstances. maxThreshold(1) - User has exceeded the threshold for consecutive number of attempts to log-in. timeThreshold(2) - User has exceeded the threshold for number of log-in failure over a pre-defined period.')
anxTrapAttackErrmsg = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapAttackErrmsg.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapAttackErrmsg.setDescription('Error message string.')
anxTrapDbErrcode = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("read-error", 1), ("write-error", 2), ("protect-error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapDbErrcode.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapDbErrcode.setDescription('Error code indicating the type of error occured when ERPCD tried to access the database. read-error(1) - ERPCD cannot read the database write-error(2) - ERPCD cannot write to the database protect-error(3) - ERPCD detects wrong database protection.')
anxTrapDbErrmsg = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: anxTrapDbErrmsg.setStatus('mandatory')
if mibBuilder.loadTexts: anxTrapDbErrmsg.setDescription('Error message string giving details about the error when ERPCD tried to access the database.')
trapModemMsg = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapModemMsg.setStatus('mandatory')
if mibBuilder.loadTexts: trapModemMsg.setDescription('This object is send along with the modem busy out trap. This object specifies the modem which is being busied out and the reason for busying out the modem.')
operImageModemImage = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: operImageModemImage.setStatus('mandatory')
if mibBuilder.loadTexts: operImageModemImage.setDescription('This is a trap indicating the operational image version and the modem image version.')
wanVersion = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanVersion.setStatus('mandatory')
if mibBuilder.loadTexts: wanVersion.setDescription('This trap indicates that a wan has come up and also the version string for that wan.')
trapAfdMsg = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 10, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAfdMsg.setStatus('mandatory')
if mibBuilder.loadTexts: trapAfdMsg.setDescription('This object is sent along with the afd catastrophic trap. This object specifies the wan module which is inoperable')
mibBuilder.exportSymbols("XYLO-TRAPOBJECTS-MIB", wanSesThreshold=wanSesThreshold, anxTrapAttackErrmsg=anxTrapAttackErrmsg, anxTrapHostEntry=anxTrapHostEntry, wanUasThreshold=wanUasThreshold, anxTrapDbErrmsg=anxTrapDbErrmsg, diallnkTrpEna=diallnkTrpEna, callEndTrapThresh=callEndTrapThresh, anxTrapPortIndex=anxTrapPortIndex, callBeginTrapObj=callBeginTrapObj, anxTrapHostStatus=anxTrapHostStatus, anxTrapPortType=anxTrapPortType, anxTrapHostComm=anxTrapHostComm, anxTrapHostTable=anxTrapHostTable, anxTrapHostNext=anxTrapHostNext, unexpectDisconnectTrapThresh=unexpectDisconnectTrapThresh, anxTrapHostAgeTime=anxTrapHostAgeTime, anxTrapInetAddr=anxTrapInetAddr, operImageModemImage=operImageModemImage, trapAfdMsg=trapAfdMsg, wanOofThreshold=wanOofThreshold, anxTrapHostIndex=anxTrapHostIndex, wanCvThreshold=wanCvThreshold, wanEsfThreshold=wanEsfThreshold, anxTrapHostCurEnt=anxTrapHostCurEnt, anxTrapAttackErrcode=anxTrapAttackErrcode, ds0ErrorThreshold=ds0ErrorThreshold, mdmErrorTrapThresh=mdmErrorTrapThresh, wanBpvThreshold=wanBpvThreshold, trapModemMsg=trapModemMsg, forcedCallDisconnectTrapThresh=forcedCallDisconnectTrapThresh, wanVersion=wanVersion, anxTrapHostPortNumber=anxTrapHostPortNumber, wanCssThreshold=wanCssThreshold, anxTrapDbErrcode=anxTrapDbErrcode, anxTrapHostAddrType=anxTrapHostAddrType, wanLofcThreshold=wanLofcThreshold, anxTrapHostNetAddr=anxTrapHostNetAddr, wanBesThreshold=wanBesThreshold, anxTrapHostMax=anxTrapHostMax, wanEsThreshold=wanEsThreshold, anxTrapUserName=anxTrapUserName, anxTrapHostGrouping=anxTrapHostGrouping)