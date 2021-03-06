#
# PySNMP MIB module ENTERASYS-CONFIGURATION-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-CONFIGURATION-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Unsigned32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, NotificationType, IpAddress, ModuleIdentity, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Unsigned32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "NotificationType", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter64", "iso")
DisplayString, DateAndTime, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "RowStatus", "TextualConvention")
etsysConfigurationManagementMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16))
etsysConfigurationManagementMIB.setRevisions(('2008-12-05 14:13', '2002-10-03 20:21', '2002-09-30 17:02', '2001-12-03 19:49',))
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setLastUpdated('200812051413Z')
if mibBuilder.loadTexts: etsysConfigurationManagementMIB.setOrganization('Enterasys Networks, Inc')
etsysConfigMgmtStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1))
etsysConfigMgmtChange = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2))
etsysConfigMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3))
class ConfigMgmtOperations(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("resetHardware", 0), ("resetSoftware", 1), ("imageDownload", 2), ("imageDownloadNonPersistent", 3), ("configurationReset", 4), ("configurationUpload", 5), ("configurationDownload", 6), ("imageSetSelected", 7), ("imageGetSelected", 8), ("configurationActivate", 9), ("configurationAppend", 10), ("configurationPersist", 11), ("configurationParse", 12), ("validationMD5sum", 13), ("bootPromDownload", 14))

etsysConfigMgmtCurrentImageURL = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 1), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtCurrentImageURL.setStatus('current')
etsysConfigMgmtCurrentConfigURL = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtCurrentConfigURL.setStatus('current')
etsysConfigMgmtPersistentStorageStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 3), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageStatus.setStatus('current')
etsysConfigMgmtPersistentStorageCkSum = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 1, 4), DisplayString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtPersistentStorageCkSum.setStatus('current')
etsysConfigMgmtChangeLimit = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeLimit.setStatus('current')
etsysConfigMgmtChangeCurrent = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCurrent.setStatus('current')
etsysConfigMgmtChangeCompleted = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompleted.setStatus('current')
etsysConfigMgmtChangeSupportedURLs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 4), Bits().clone(namedValues=NamedValues(("etsysConfigMgmtFtp", 0), ("etsysConfigMgmtRcp", 1), ("etsysConfigMgmtHttp", 2), ("etsysConfigMgmtTftp", 3), ("etsysConfigMgmtFile", 4), ("etsysConfigMgmtBootP", 5), ("etsysConfigMgmtScp", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedURLs.setStatus('current')
etsysConfigMgmtChangeSupportedOperations = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 5), ConfigMgmtOperations()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeSupportedOperations.setStatus('current')
etsysConfigMgmtChangeNextAvailableIndex = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeNextAvailableIndex.setStatus('current')
etsysConfigMgmtChangeTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7), )
if mibBuilder.loadTexts: etsysConfigMgmtChangeTable.setStatus('current')
etsysConfigMgmtChangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1), ).setIndexNames((0, "ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeIndex"))
if mibBuilder.loadTexts: etsysConfigMgmtChangeEntry.setStatus('current')
etsysConfigMgmtChangeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysConfigMgmtChangeIndex.setStatus('current')
etsysConfigMgmtChangeURL = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 2), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeURL.setStatus('current')
etsysConfigMgmtChangeOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 3), ConfigMgmtOperations()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperation.setStatus('current')
etsysConfigMgmtChangeOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inactive", 1), ("pending", 2), ("running", 3), ("success", 4), ("failure", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeOperStatus.setStatus('current')
etsysConfigMgmtChangeDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeDelayTime.setStatus('current')
etsysConfigMgmtChangeEnqueuedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 6), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeEnqueuedTime.setStatus('current')
etsysConfigMgmtChangeCompletionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 7), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeCompletionTime.setStatus('current')
etsysConfigMgmtChangeBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeBytesTransferred.setStatus('current')
etsysConfigMgmtChangeValidationString = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 9), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeValidationString.setStatus('current')
etsysConfigMgmtChangeErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 10), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigMgmtChangeErrorDescription.setStatus('current')
etsysConfigMgmtChangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 2, 7, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysConfigMgmtChangeRowStatus.setStatus('current')
etsysConfigMgmtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1))
etsysConfigMgmtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2))
etsysConfigMgmtStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 1)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentImageURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtCurrentConfigURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageStatus"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtPersistentStorageCkSum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtStatusGroup = etsysConfigMgmtStatusGroup.setStatus('current')
etsysConfigMgmtChangeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 1, 2)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeLimit"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCurrent"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompleted"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedURLs"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeSupportedOperations"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeNextAvailableIndex"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeURL"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperation"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeOperStatus"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeDelayTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeEnqueuedTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeCompletionTime"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeBytesTransferred"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeValidationString"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeErrorDescription"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtChangeGroup = etsysConfigMgmtChangeGroup.setStatus('current')
etsysConfigMgmtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 16, 3, 2, 1)).setObjects(("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtStatusGroup"), ("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", "etsysConfigMgmtChangeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigMgmtCompliance = etsysConfigMgmtCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-CONFIGURATION-MANAGEMENT-MIB", etsysConfigMgmtConformance=etsysConfigMgmtConformance, etsysConfigMgmtChangeRowStatus=etsysConfigMgmtChangeRowStatus, etsysConfigMgmtChangeGroup=etsysConfigMgmtChangeGroup, etsysConfigMgmtChangeCompleted=etsysConfigMgmtChangeCompleted, etsysConfigMgmtChangeLimit=etsysConfigMgmtChangeLimit, etsysConfigMgmtChangeErrorDescription=etsysConfigMgmtChangeErrorDescription, etsysConfigMgmtPersistentStorageStatus=etsysConfigMgmtPersistentStorageStatus, etsysConfigMgmtGroups=etsysConfigMgmtGroups, etsysConfigMgmtChangeURL=etsysConfigMgmtChangeURL, etsysConfigMgmtStatusGroup=etsysConfigMgmtStatusGroup, etsysConfigMgmtChange=etsysConfigMgmtChange, etsysConfigMgmtChangeSupportedURLs=etsysConfigMgmtChangeSupportedURLs, etsysConfigMgmtCompliances=etsysConfigMgmtCompliances, etsysConfigMgmtChangeTable=etsysConfigMgmtChangeTable, etsysConfigMgmtChangeDelayTime=etsysConfigMgmtChangeDelayTime, etsysConfigMgmtChangeBytesTransferred=etsysConfigMgmtChangeBytesTransferred, etsysConfigurationManagementMIB=etsysConfigurationManagementMIB, etsysConfigMgmtChangeNextAvailableIndex=etsysConfigMgmtChangeNextAvailableIndex, etsysConfigMgmtCurrentImageURL=etsysConfigMgmtCurrentImageURL, PYSNMP_MODULE_ID=etsysConfigurationManagementMIB, etsysConfigMgmtChangeEntry=etsysConfigMgmtChangeEntry, etsysConfigMgmtChangeCompletionTime=etsysConfigMgmtChangeCompletionTime, etsysConfigMgmtChangeValidationString=etsysConfigMgmtChangeValidationString, etsysConfigMgmtCompliance=etsysConfigMgmtCompliance, etsysConfigMgmtChangeOperation=etsysConfigMgmtChangeOperation, etsysConfigMgmtChangeSupportedOperations=etsysConfigMgmtChangeSupportedOperations, ConfigMgmtOperations=ConfigMgmtOperations, etsysConfigMgmtChangeCurrent=etsysConfigMgmtChangeCurrent, etsysConfigMgmtChangeEnqueuedTime=etsysConfigMgmtChangeEnqueuedTime, etsysConfigMgmtCurrentConfigURL=etsysConfigMgmtCurrentConfigURL, etsysConfigMgmtPersistentStorageCkSum=etsysConfigMgmtPersistentStorageCkSum, etsysConfigMgmtStatus=etsysConfigMgmtStatus, etsysConfigMgmtChangeIndex=etsysConfigMgmtChangeIndex, etsysConfigMgmtChangeOperStatus=etsysConfigMgmtChangeOperStatus)
