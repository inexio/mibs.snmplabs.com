#
# PySNMP MIB module CISCO-VOICE-APPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-APPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, ObjectIdentity, Counter64, NotificationType, ModuleIdentity, Counter32, Integer32, MibIdentifier, iso, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "ObjectIdentity", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "Integer32", "MibIdentifier", "iso", "Gauge32", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoVoiceAppsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 190))
ciscoVoiceAppsMIB.setRevisions(('2005-12-22 00:00', '2001-02-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setRevisionsDescriptions(('Imported Unsigned32 from SNMPv2-SMI instead of CISCO-TC.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setLastUpdated('200512220000Z')
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-selsius@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceAppsMIB.setDescription('The MIB Module for the management of Cisco Voice Applications. This MIB is designed to work in conjunction with the SYSAPPL-MIB to provide status monitoring, provisioning and notification.')
ciscoVoiceAppsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1))
cvaGeneralInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1))
cvaModuleFailureInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2))
cvaWorkflowInstallTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1), )
if mibBuilder.loadTexts: cvaWorkflowInstallTable.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallTable.setDescription('The table containing the list of installed Workflow applications provisioned on the media server. For instance, this table may contain an entry for each of the Auto Attendant(AA) or Integrated Contact Distribution(ICD) application installed on the Cisco Workflow Application.')
cvaWorkflowInstallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallIndex"))
if mibBuilder.loadTexts: cvaWorkflowInstallEntry.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallEntry.setDescription('An entry (conceptual row) in the Workflow Installation Table, containing information associated with the Cisco Workflow Application. This entry is created when a workflow application is installed via the application Administration page.')
cvaWorkflowInstallIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cvaWorkflowInstallIndex.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallIndex.setDescription('An arbitrary integer which uniquely identifies an Workflow Application.')
cvaWorkflowInstallName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallName.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallName.setDescription('The name of the workflow application.')
cvaWorkflowInstallLocator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallLocator.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallLocator.setDescription('The extension number or CTI (Computer Telephony Integration) route point associated with the workflow application. For instance, 5000 for extension 5000.')
cvaWorkflowInstallScriptName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallScriptName.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallScriptName.setDescription('The workflow application script name.')
cvaWorkflowInstallEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvaWorkflowInstallEnable.setStatus('current')
if mibBuilder.loadTexts: cvaWorkflowInstallEnable.setDescription('The status of the workflow application. true(1): Workflow Application is enabled false(2): Workflow Application is disabled.')
cvaNotificationEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvaNotificationEnable.setStatus('current')
if mibBuilder.loadTexts: cvaNotificationEnable.setDescription('To enable(1) or disable(2) generation of the following notifications: cvaModuleStart notification cvaModuleStop notification cvaModuleRunTimeFailure notification cvaProcessStart notification cvaProcessStop notification The default value is enable(1).')
cvaAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: cvaAlarmSeverity.setDescription('The application alarm notification severity code. emergency: System unusable alert: Immediate response needed critical: Critical condition error: Error condition warning: Warning condition notice: Normal but significant condition informational: Informational situation.')
cvaModuleName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleName.setStatus('current')
if mibBuilder.loadTexts: cvaModuleName.setDescription('The application module or subsystem name.')
cvaProcessId = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaProcessId.setStatus('current')
if mibBuilder.loadTexts: cvaProcessId.setDescription("A unique value for each of the process running on the host. Wherever possible, this should be the system's native, unique Identification number (process id).")
cvaModuleFailureName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureName.setStatus('current')
if mibBuilder.loadTexts: cvaModuleFailureName.setDescription('The application module name which causes the failure.')
cvaModuleFailureCause = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("gracefulShutDown", 2), ("heartBeatFailure", 3), ("initFailure", 4), ("outOfResource", 5), ("partialFailure", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureCause.setStatus('current')
if mibBuilder.loadTexts: cvaModuleFailureCause.setDescription('The application module failure cause code. This is used by cvaModuleStop to indicate reason of module stop if known. other: Other unspecified failure cause gracefulShutDown: Module is gracefully shut down heartBeatStopped: Module heart beat stopped is detected initFailure: Module is failed during initialization outOfResource: Module is failed due to out of resource partialFailure: Module partially failure is detected.')
cvaModuleFailureMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleFailureMessage.setStatus('current')
if mibBuilder.loadTexts: cvaModuleFailureMessage.setDescription('The application module failure message.')
cvaModuleRunTimeFailureCause = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("readAccessFailure", 2), ("writeAccessFailure", 3), ("createFailure", 4), ("deleteFailure", 5), ("updateFailure", 6), ("initFailure", 7), ("loadFailure", 8), ("outOfResource", 9), ("callProcessFailure", 10), ("registrationFailure", 11), ("deRegistrationFailure", 12), ("connectionFailure", 13), ("disconnectionFailure", 14), ("unknownTarget", 15), ("unReacheableTarget", 16)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cvaModuleRunTimeFailureCause.setStatus('current')
if mibBuilder.loadTexts: cvaModuleRunTimeFailureCause.setDescription('The application module run-time failure cause code. other: Other or unspecified failure readAccessFailure: Read Access failure writeAccessFailure: Write Access failure createFailure: Resource Creation failure deleteFailure: Resource Deletion failure updateFailure: Update failure initFailure: Initialization failure loadFailure: Resource Load failure outOfResource: Out of Resource callProcessFailure: Call Processing failure registrationFailure: Registration failure deRegistrationFailure: De-Registration failure connectionFailure: Connection failure disconnectionFailure: Desconnection failure unknownTarget: Unknown Target/destination unReacheableTarget: UnReacheable Target/destination')
ciscoVoiceAppsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 2))
ciscoVoiceAppsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0))
cvaModuleStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"))
if mibBuilder.loadTexts: cvaModuleStart.setStatus('current')
if mibBuilder.loadTexts: cvaModuleStart.setDescription('A cvaModuleStart notification signifies that an application module or subsystem has successfully started and transitioned into in-service state. This notification is working in conjunction with the cvaModuleStop notification to notify the start and stop status of a particular application module.')
cvaModuleStop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 2)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
if mibBuilder.loadTexts: cvaModuleStop.setStatus('current')
if mibBuilder.loadTexts: cvaModuleStop.setDescription('A cvaModuleStop notification signifies that an application module or subsystem has stopped. This notification is working in conjunction with the cvaModuleStart notification to notify the start and stop status of a particular application module. If failure cause is known then it will be specified in the cvaModuleFailureCause variable. Additional failure information associated with cvaModuleFailureCause can be specified in the cvaModuleFailureCauseMessage.')
cvaModuleRunTimeFailure = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 3)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
if mibBuilder.loadTexts: cvaModuleRunTimeFailure.setStatus('current')
if mibBuilder.loadTexts: cvaModuleRunTimeFailure.setDescription('A cvaModuleRunTimeFailure notification signifies that a run time failure has occurred. If failure cause is known then it will be specified in the cvaModuleRunTimeFailureCause variable. Additional failure information associated with cvaModuleRunTimeFailureCause can be specified in the cvaModuleFailureCauseMessage.')
cvaProcessStart = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 4)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
if mibBuilder.loadTexts: cvaProcessStart.setStatus('current')
if mibBuilder.loadTexts: cvaProcessStart.setDescription('A cvaProcessStart notification signifies that a process has just started. This notification is intended to work in conjunction with the caProcessStop notification to notify the start and stop status of a particular process.')
cvaProcessStop = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 5)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
if mibBuilder.loadTexts: cvaProcessStop.setStatus('current')
if mibBuilder.loadTexts: cvaProcessStop.setDescription('A cvaProcessStop notification signifies that a process has just stopped. This notification is intended to work in conjunction with the cvaProcessStart notification to notify the start and stop status of a particular process.')
ciscoVoiceAppsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3))
ciscoVoiceAppsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1))
ciscoVoiceAppsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2))
ciscoVoiceAppsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaModuleInfoGroup"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationInfoGroup"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAppsMIBCompliance = ciscoVoiceAppsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVoiceAppsMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO APPLICATION MIB.')
cvaModuleInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 1)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallName"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallLocator"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallScriptName"), ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallEnable"), ("CISCO-VOICE-APPS-MIB", "cvaNotificationEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaModuleInfoGroup = cvaModuleInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cvaModuleInfoGroup.setDescription('A collection of objects which provide info about the application. It comprises of all the modules and servers associated with the application.')
cvaNotificationInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 2)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"), ("CISCO-VOICE-APPS-MIB", "cvaModuleName"), ("CISCO-VOICE-APPS-MIB", "cvaProcessId"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"), ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaNotificationInfoGroup = cvaNotificationInfoGroup.setStatus('current')
if mibBuilder.loadTexts: cvaNotificationInfoGroup.setDescription('A collection of notification objects which provide info about the application notification.')
cvaNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 3)).setObjects(("CISCO-VOICE-APPS-MIB", "cvaModuleStart"), ("CISCO-VOICE-APPS-MIB", "cvaModuleStop"), ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailure"), ("CISCO-VOICE-APPS-MIB", "cvaProcessStart"), ("CISCO-VOICE-APPS-MIB", "cvaProcessStop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvaNotificationGroup = cvaNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: cvaNotificationGroup.setDescription('A collection of notifications.')
mibBuilder.exportSymbols("CISCO-VOICE-APPS-MIB", cvaModuleName=cvaModuleName, PYSNMP_MODULE_ID=ciscoVoiceAppsMIB, cvaNotificationGroup=cvaNotificationGroup, cvaModuleRunTimeFailureCause=cvaModuleRunTimeFailureCause, ciscoVoiceAppsMIBNotificationPrefix=ciscoVoiceAppsMIBNotificationPrefix, cvaNotificationInfoGroup=cvaNotificationInfoGroup, cvaWorkflowInstallEnable=cvaWorkflowInstallEnable, cvaProcessId=cvaProcessId, ciscoVoiceAppsMIBConformance=ciscoVoiceAppsMIBConformance, cvaWorkflowInstallScriptName=cvaWorkflowInstallScriptName, cvaWorkflowInstallLocator=cvaWorkflowInstallLocator, cvaProcessStart=cvaProcessStart, cvaModuleFailureMessage=cvaModuleFailureMessage, ciscoVoiceAppsMIBObjects=ciscoVoiceAppsMIBObjects, cvaWorkflowInstallName=cvaWorkflowInstallName, cvaWorkflowInstallEntry=cvaWorkflowInstallEntry, cvaModuleInfoGroup=cvaModuleInfoGroup, cvaModuleFailureCause=cvaModuleFailureCause, cvaNotificationEnable=cvaNotificationEnable, cvaModuleRunTimeFailure=cvaModuleRunTimeFailure, ciscoVoiceAppsMIBGroups=ciscoVoiceAppsMIBGroups, cvaModuleStart=cvaModuleStart, cvaModuleFailureInfo=cvaModuleFailureInfo, cvaGeneralInfo=cvaGeneralInfo, cvaProcessStop=cvaProcessStop, cvaModuleStop=cvaModuleStop, cvaAlarmSeverity=cvaAlarmSeverity, cvaWorkflowInstallIndex=cvaWorkflowInstallIndex, ciscoVoiceAppsMIB=ciscoVoiceAppsMIB, ciscoVoiceAppsMIBCompliances=ciscoVoiceAppsMIBCompliances, ciscoVoiceAppsMIBNotifications=ciscoVoiceAppsMIBNotifications, cvaWorkflowInstallTable=cvaWorkflowInstallTable, ciscoVoiceAppsMIBCompliance=ciscoVoiceAppsMIBCompliance, cvaModuleFailureName=cvaModuleFailureName)
