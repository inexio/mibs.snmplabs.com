#
# PySNMP MIB module TPT-SMS-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-SMS-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, MibIdentifier, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, Bits, IpAddress, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "Bits", "IpAddress", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_reg, = mibBuilder.importSymbols("TIPPINGPOINT-REG-MIB", "tpt-reg")
tpt_sms_groups, tpt_sms_eventsV2, tpt_smsMIBs, tpt_sms_notifypayload = mibBuilder.importSymbols("TPT-SMSMIBS", "tpt-sms-groups", "tpt-sms-eventsV2", "tpt-smsMIBs", "tpt-sms-notifypayload")
tptSmsTrapsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 4, 4))
if mibBuilder.loadTexts: tptSmsTrapsModule.setLastUpdated('0508301900Z')
if mibBuilder.loadTexts: tptSmsTrapsModule.setOrganization('TippingPoint Technologies, Inc.')
if mibBuilder.loadTexts: tptSmsTrapsModule.setContactInfo('www.tippingpoint.com')
if mibBuilder.loadTexts: tptSmsTrapsModule.setDescription("The following describes the notifications sent to and from an SMS box. Copyright 2001-2005 TippingPoint Technologies, Inc. All rights reserved. This document contains confidential and proprietary information to TippingPoint Technologies, Inc. Use of this document is subject to the terms and conditions of TippingPoint's Non-Disclosure Agreement.")
tptSmsQuarantineRequest = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 1)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
if mibBuilder.loadTexts: tptSmsQuarantineRequest.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineRequest.setDescription('SMS asking an external NMS to quarantine an endstation using the data embedded in the request')
tptSmsQuarantineAck = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 2)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
if mibBuilder.loadTexts: tptSmsQuarantineAck.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineAck.setDescription('External NMS notifying the SMS that a previously quarantine request was processed.')
tptSmsQuarantineReleaseRequest = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 3)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
if mibBuilder.loadTexts: tptSmsQuarantineReleaseRequest.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineReleaseRequest.setDescription('SMS asking an external NMS to unquarantine an endstation using the data embedded in the request')
tptSmsQuarantineReleaseAck = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 4)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"))
if mibBuilder.loadTexts: tptSmsQuarantineReleaseAck.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineReleaseAck.setDescription('External NMS notifying the SMS that a previously unquarantine request was processed.')
tptSmsQuarantinePolicyNotification = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 5)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyMatchData"))
if mibBuilder.loadTexts: tptSmsQuarantinePolicyNotification.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantinePolicyNotification.setDescription('SMS sending notification of a policy match')
tptSmsUnQuarantineRequest = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 6)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceIP"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceMAC"))
if mibBuilder.loadTexts: tptSmsUnQuarantineRequest.setStatus('current')
if mibBuilder.loadTexts: tptSmsUnQuarantineRequest.setDescription('Inverse of tptSMSQuarantineCommand - command the SMS to unquarantine an endstation. You can explicitly specify a quarantined host ID if you know it; otherwise, you may specify the IP only, in which case the SMS will look up the MAC; or the IP+MAC.')
tptSmsQuarantineCommand = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 14)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineDeviceIP"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyName"))
if mibBuilder.loadTexts: tptSmsQuarantineCommand.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineCommand.setDescription('Inverse of tptSmsUnquarantineRequest Command the SMS to quarantine an endstation. SMS will look up the MAC.')
tptSmsBoot = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 7))
if mibBuilder.loadTexts: tptSmsBoot.setStatus('current')
if mibBuilder.loadTexts: tptSmsBoot.setDescription('SMS: system has booted')
tptSmsReboot = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 8))
if mibBuilder.loadTexts: tptSmsReboot.setStatus('current')
if mibBuilder.loadTexts: tptSmsReboot.setDescription('SMS: system is rebooting')
tptSmsShuttingDown = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 9))
if mibBuilder.loadTexts: tptSmsShuttingDown.setStatus('current')
if mibBuilder.loadTexts: tptSmsShuttingDown.setDescription('SMS: system is shutting down')
tptSmsReady = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 10))
if mibBuilder.loadTexts: tptSmsReady.setStatus('current')
if mibBuilder.loadTexts: tptSmsReady.setDescription('SMS: system is ready')
tptSmsAuthenticationError = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 11))
if mibBuilder.loadTexts: tptSmsAuthenticationError.setStatus('current')
if mibBuilder.loadTexts: tptSmsAuthenticationError.setDescription('SMS: authentication error')
tptSmsEgpNeighborDownstate = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 12))
if mibBuilder.loadTexts: tptSmsEgpNeighborDownstate.setStatus('current')
if mibBuilder.loadTexts: tptSmsEgpNeighborDownstate.setDescription('SMS: EGP neighbor to downstate')
tptSmsSystemRestart = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 13))
if mibBuilder.loadTexts: tptSmsSystemRestart.setStatus('current')
if mibBuilder.loadTexts: tptSmsSystemRestart.setDescription('SMS: server process has restarted')
tptSmsRepDvVerifySuccess = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 15)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsRepDvVersion"), ("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptSmsRepDvVerifySuccess.setStatus('current')
if mibBuilder.loadTexts: tptSmsRepDvVerifySuccess.setDescription('SMS: Reputation DV downloaded and verified.')
tptSmsRepDvVerifyFail = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 16)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsRepDvVersion"), ("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptSmsRepDvVerifyFail.setStatus('current')
if mibBuilder.loadTexts: tptSmsRepDvVerifyFail.setDescription('SMS: Reputation DV downloaded. Verification failed.')
tptSmsTest = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 17)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptSmsTest.setStatus('current')
if mibBuilder.loadTexts: tptSmsTest.setDescription('SMS: Test trap.')
tptSmsRebootingDevice = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 18)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptSmsRebootingDevice.setStatus('current')
if mibBuilder.loadTexts: tptSmsRebootingDevice.setDescription('SMS is rebooting a device.')
tptDeviceNonComm = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 19)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptDeviceNonComm.setStatus('current')
if mibBuilder.loadTexts: tptDeviceNonComm.setDescription('SMS has lost communications with a device.')
tptDeviceBooted = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 0, 20)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsMessage"))
if mibBuilder.loadTexts: tptDeviceBooted.setStatus('current')
if mibBuilder.loadTexts: tptDeviceBooted.setDescription('A device has rebooted.')
tptSmsQuarantineNotifyId = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyId.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyId.setDescription('A unique incrementing integer assigned for each quarantine event.')
tptSmsQuarantineNotifyData = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 2), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyData.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyData.setDescription('A string consisting of the parameters used to identify the device to quarantine. The format is NAME:VALUE with multiple parameters separated by a newline')
tptSmsQuarantinePolicyMatchData = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 3), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantinePolicyMatchData.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantinePolicyMatchData.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantineNotifyType = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyType.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyType.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantineDeviceIP = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineDeviceIP.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineDeviceIP.setDescription('An IP address used as a trap parameter.')
tptSmsQuarantineDeviceMAC = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 6), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineDeviceMAC.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineDeviceMAC.setDescription('A MAC address used a a trap parameter')
tptSmsQuarantineSwitchPort = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 7), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineSwitchPort.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineSwitchPort.setDescription('A port number or index used as a trap parameter')
tptSmsQuarantineEndpointUser = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineEndpointUser.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineEndpointUser.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantineNotifyActionList = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 9), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyActionList.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyActionList.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantineNotifyParamList = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyParamList.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyParamList.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantineNotifyOptionList = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 11), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantineNotifyOptionList.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyOptionList.setDescription('A string consisting of the parameters used to identify the matching policy')
tptSmsQuarantinePolicyName = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 12), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsQuarantinePolicyName.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantinePolicyName.setDescription('The name of an SMS Quarantine Policy. If the named policy does not exists on the SMS, a default will be chosen.')
tptSmsRepDvVersion = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 13), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsRepDvVersion.setStatus('current')
if mibBuilder.loadTexts: tptSmsRepDvVersion.setDescription('The Rep DV version.')
tptSmsMessage = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 4, 3, 1, 14), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: tptSmsMessage.setStatus('current')
if mibBuilder.loadTexts: tptSmsMessage.setDescription('A generic message parameter.')
tptSmsQuarantineDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 1)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyId"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineNotifyData"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyMatchData"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptSmsQuarantineDataGroup = tptSmsQuarantineDataGroup.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineDataGroup.setDescription('Payload of SMS quarantine traps consisting of a unique identifier and a parseable string')
tptSmsQuarantineNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 2)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineRequest"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineReleaseRequest"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantinePolicyNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptSmsQuarantineNotifyGroup = tptSmsQuarantineNotifyGroup.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyGroup.setDescription('SMS quarantine traps sent to an NMS to indicate devices that require a quarantine operation')
tptSmsQuarantineNotifyAckGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 3)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineAck"), ("TPT-SMS-TRAP-MIB", "tptSmsQuarantineReleaseAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptSmsQuarantineNotifyAckGroup = tptSmsQuarantineNotifyAckGroup.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineNotifyAckGroup.setDescription('SMS quarantine traps sent to an SMS system to indicate devices that have been quarantined')
tptSmsQuarantineRequestGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10734, 3, 4, 1, 1, 4)).setObjects(("TPT-SMS-TRAP-MIB", "tptSmsQuarantineCommand"), ("TPT-SMS-TRAP-MIB", "tptSmsUnQuarantineRequest"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tptSmsQuarantineRequestGroup = tptSmsQuarantineRequestGroup.setStatus('current')
if mibBuilder.loadTexts: tptSmsQuarantineRequestGroup.setDescription('SMS quarantine traps received to indicate devices that require a (un)quarantine operation')
mibBuilder.exportSymbols("TPT-SMS-TRAP-MIB", tptSmsQuarantineNotifyAckGroup=tptSmsQuarantineNotifyAckGroup, tptSmsQuarantinePolicyNotification=tptSmsQuarantinePolicyNotification, tptSmsQuarantineNotifyGroup=tptSmsQuarantineNotifyGroup, PYSNMP_MODULE_ID=tptSmsTrapsModule, tptSmsQuarantineSwitchPort=tptSmsQuarantineSwitchPort, tptSmsTrapsModule=tptSmsTrapsModule, tptDeviceBooted=tptDeviceBooted, tptSmsQuarantineRequest=tptSmsQuarantineRequest, tptSmsQuarantineNotifyParamList=tptSmsQuarantineNotifyParamList, tptSmsQuarantineNotifyType=tptSmsQuarantineNotifyType, tptSmsTest=tptSmsTest, tptSmsRepDvVerifyFail=tptSmsRepDvVerifyFail, tptSmsShuttingDown=tptSmsShuttingDown, tptSmsRepDvVerifySuccess=tptSmsRepDvVerifySuccess, tptSmsQuarantineDeviceMAC=tptSmsQuarantineDeviceMAC, tptSmsSystemRestart=tptSmsSystemRestart, tptSmsQuarantineReleaseRequest=tptSmsQuarantineReleaseRequest, tptSmsQuarantineReleaseAck=tptSmsQuarantineReleaseAck, tptSmsAuthenticationError=tptSmsAuthenticationError, tptSmsQuarantineCommand=tptSmsQuarantineCommand, tptSmsQuarantineNotifyId=tptSmsQuarantineNotifyId, tptSmsQuarantinePolicyMatchData=tptSmsQuarantinePolicyMatchData, tptDeviceNonComm=tptDeviceNonComm, tptSmsRepDvVersion=tptSmsRepDvVersion, tptSmsMessage=tptSmsMessage, tptSmsQuarantineNotifyActionList=tptSmsQuarantineNotifyActionList, tptSmsQuarantineDataGroup=tptSmsQuarantineDataGroup, tptSmsReboot=tptSmsReboot, tptSmsUnQuarantineRequest=tptSmsUnQuarantineRequest, tptSmsBoot=tptSmsBoot, tptSmsQuarantineRequestGroup=tptSmsQuarantineRequestGroup, tptSmsQuarantineAck=tptSmsQuarantineAck, tptSmsReady=tptSmsReady, tptSmsRebootingDevice=tptSmsRebootingDevice, tptSmsQuarantineNotifyData=tptSmsQuarantineNotifyData, tptSmsQuarantineEndpointUser=tptSmsQuarantineEndpointUser, tptSmsQuarantinePolicyName=tptSmsQuarantinePolicyName, tptSmsEgpNeighborDownstate=tptSmsEgpNeighborDownstate, tptSmsQuarantineDeviceIP=tptSmsQuarantineDeviceIP, tptSmsQuarantineNotifyOptionList=tptSmsQuarantineNotifyOptionList)
