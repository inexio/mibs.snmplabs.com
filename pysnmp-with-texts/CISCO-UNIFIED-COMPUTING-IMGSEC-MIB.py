#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-IMGSEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-UNIFIED-COMPUTING-IMGSEC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:16:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, CiscoInetAddressMask, CiscoAlarmSeverity, TimeIntervalSec, Unsigned64 = mibBuilder.importSymbols("CISCO-TC", "CiscoNetworkAddress", "CiscoInetAddressMask", "CiscoAlarmSeverity", "TimeIntervalSec", "Unsigned64")
ciscoUnifiedComputingMIBObjects, CucsManagedObjectId, CucsManagedObjectDn = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIBObjects", "CucsManagedObjectId", "CucsManagedObjectDn")
CucsPolicyPolicyOwner, CucsImgsecKeyType = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-TC-MIB", "CucsPolicyPolicyOwner", "CucsImgsecKeyType")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, iso, Bits, ModuleIdentity, Unsigned32, Integer32, TimeTicks, NotificationType, IpAddress, MibIdentifier, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "Bits", "ModuleIdentity", "Unsigned32", "Integer32", "TimeTicks", "NotificationType", "IpAddress", "MibIdentifier", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, DateAndTime, RowPointer, DisplayString, TruthValue, MacAddress, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DateAndTime", "RowPointer", "DisplayString", "TruthValue", "MacAddress", "TextualConvention", "TimeInterval")
cucsImgsecObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56))
if mibBuilder.loadTexts: cucsImgsecObjects.setLastUpdated('201601180000Z')
if mibBuilder.loadTexts: cucsImgsecObjects.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: cucsImgsecObjects.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cucsImgsecObjects.setDescription('MIB representation of the Cisco Unified Computing System IMGSEC management information model package')
cucsImgsecKeyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1), )
if mibBuilder.loadTexts: cucsImgsecKeyTable.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyTable.setDescription('Cisco UCS imgsec:Key managed object table')
cucsImgsecKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-IMGSEC-MIB", "cucsImgsecKeyInstanceId"))
if mibBuilder.loadTexts: cucsImgsecKeyEntry.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyEntry.setDescription('Entry for the cucsImgsecKeyTable table.')
cucsImgsecKeyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsImgsecKeyInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyInstanceId.setDescription('Instance identifier of the managed object.')
cucsImgsecKeyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecKeyDn.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyDn.setDescription('Cisco UCS imgsec:Key:dn managed object property')
cucsImgsecKeyRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecKeyRn.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyRn.setDescription('Cisco UCS imgsec:Key:rn managed object property')
cucsImgsecKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 4), CucsImgsecKeyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecKeyType.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyType.setDescription('Cisco UCS imgsec:Key:type managed object property')
cucsImgsecKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecKeyValue.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecKeyValue.setDescription('Cisco UCS imgsec:Key:value managed object property')
cucsImgsecPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2), )
if mibBuilder.loadTexts: cucsImgsecPolicyTable.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyTable.setDescription('Cisco UCS imgsec:Policy managed object table')
cucsImgsecPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1), ).setIndexNames((0, "CISCO-UNIFIED-COMPUTING-IMGSEC-MIB", "cucsImgsecPolicyInstanceId"))
if mibBuilder.loadTexts: cucsImgsecPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyEntry.setDescription('Entry for the cucsImgsecPolicyTable table.')
cucsImgsecPolicyInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 1), CucsManagedObjectId())
if mibBuilder.loadTexts: cucsImgsecPolicyInstanceId.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyInstanceId.setDescription('Instance identifier of the managed object.')
cucsImgsecPolicyDn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 2), CucsManagedObjectDn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyDn.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyDn.setDescription('Cisco UCS imgsec:Policy:dn managed object property')
cucsImgsecPolicyRn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyRn.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyRn.setDescription('Cisco UCS imgsec:Policy:rn managed object property')
cucsImgsecPolicyDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyDescr.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyDescr.setDescription('Cisco UCS imgsec:Policy:descr managed object property')
cucsImgsecPolicyIntId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyIntId.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyIntId.setDescription('Cisco UCS imgsec:Policy:intId managed object property')
cucsImgsecPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyName.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyName.setDescription('Cisco UCS imgsec:Policy:name managed object property')
cucsImgsecPolicyPolicyLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyPolicyLevel.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyPolicyLevel.setDescription('Cisco UCS imgsec:Policy:policyLevel managed object property')
cucsImgsecPolicyPolicyOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 8), CucsPolicyPolicyOwner()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cucsImgsecPolicyPolicyOwner.setStatus('current')
if mibBuilder.loadTexts: cucsImgsecPolicyPolicyOwner.setDescription('Cisco UCS imgsec:Policy:policyOwner managed object property')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-IMGSEC-MIB", cucsImgsecPolicyIntId=cucsImgsecPolicyIntId, cucsImgsecPolicyRn=cucsImgsecPolicyRn, cucsImgsecPolicyInstanceId=cucsImgsecPolicyInstanceId, cucsImgsecKeyInstanceId=cucsImgsecKeyInstanceId, cucsImgsecKeyValue=cucsImgsecKeyValue, cucsImgsecPolicyPolicyOwner=cucsImgsecPolicyPolicyOwner, cucsImgsecPolicyDn=cucsImgsecPolicyDn, cucsImgsecKeyTable=cucsImgsecKeyTable, cucsImgsecPolicyName=cucsImgsecPolicyName, cucsImgsecObjects=cucsImgsecObjects, cucsImgsecKeyRn=cucsImgsecKeyRn, cucsImgsecKeyDn=cucsImgsecKeyDn, PYSNMP_MODULE_ID=cucsImgsecObjects, cucsImgsecKeyType=cucsImgsecKeyType, cucsImgsecKeyEntry=cucsImgsecKeyEntry, cucsImgsecPolicyTable=cucsImgsecPolicyTable, cucsImgsecPolicyEntry=cucsImgsecPolicyEntry, cucsImgsecPolicyPolicyLevel=cucsImgsecPolicyPolicyLevel, cucsImgsecPolicyDescr=cucsImgsecPolicyDescr)