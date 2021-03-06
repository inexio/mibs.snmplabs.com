#
# PySNMP MIB module QB-QOS-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QB-QOS-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:43:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
qbMibs, = mibBuilder.importSymbols("QUANTUMBRIDGE-REG", "qbMibs")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, TimeTicks, ObjectIdentity, IpAddress, Unsigned32, Gauge32, Bits, MibIdentifier, iso, ModuleIdentity, Counter32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "Unsigned32", "Gauge32", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "Counter32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
qbQosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4323, 2, 14))
if mibBuilder.loadTexts: qbQosMIB.setLastUpdated('0101022155Z')
if mibBuilder.loadTexts: qbQosMIB.setOrganization('Quantum Bridge')
if mibBuilder.loadTexts: qbQosMIB.setContactInfo('mvaysman@quantumbridge.com')
if mibBuilder.loadTexts: qbQosMIB.setDescription("This module defines objects for the management of QB's proprietary QOS capability. This capability is based on Policing and Thresholding. The purpose of the QB Quality of Service (qos) function is to share access to an interface's bandwidth based on policies set up by the administrator.")
class QbMbitRate(TextualConvention, Integer32):
    description = 'A data rate in Mbits/second.'
    status = 'current'

qbQosObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1))
qbQosNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 2))
qbQosConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3))
qbQosIfConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1))
qbQosIfConfTableLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfConfTableLastUpdate.setStatus('current')
if mibBuilder.loadTexts: qbQosIfConfTableLastUpdate.setDescription('The value of sysUpTime at the time of the last creation, deletion or modification of an entry in the qbQosIfConfTable. If the number of entries has been unchanged since the last re-initialization of the agent, then this object contains a zero value.')
qbQosIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2), )
if mibBuilder.loadTexts: qbQosIfConfTable.setStatus('current')
if mibBuilder.loadTexts: qbQosIfConfTable.setDescription('This table provides statistics for OAS300 Ethernet switching ports. Note that the table does not contain information about IOT ethernet ports.')
qbQosIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qbQosIfConfEntry.setStatus('current')
if mibBuilder.loadTexts: qbQosIfConfEntry.setDescription('Configuration information about a single ethernet switching port')
qbQosIfConfPolicingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbQosIfConfPolicingAdminStatus.setStatus('current')
if mibBuilder.loadTexts: qbQosIfConfPolicingAdminStatus.setDescription('The object is used to enable or disable policing policy on a given port.')
qbQosIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2), )
if mibBuilder.loadTexts: qbQosIfStatTable.setStatus('current')
if mibBuilder.loadTexts: qbQosIfStatTable.setDescription('This table provides statistics for OAS300 Ethernet switching ports. Note that the table does not contain information about IOT ethernet ports.')
qbQosIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qbQosIfStatEntry.setStatus('current')
if mibBuilder.loadTexts: qbQosIfStatEntry.setDescription('Statistics about a single ethernet switching port')
qbQosIfStatDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatDiscPkts.setStatus('current')
if mibBuilder.loadTexts: qbQosIfStatDiscPkts.setDescription('A count of the number of packets discarded for this interface due to policing on this interface.')
qbQosIfStatUpThreshDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatUpThreshDiscPkts.setStatus('current')
if mibBuilder.loadTexts: qbQosIfStatUpThreshDiscPkts.setDescription('A count of the number of upstream packets discarded for this interface due to thresholding on this interface.')
qbQosIfStatDownThreshDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatDownThreshDiscPkts.setStatus('current')
if mibBuilder.loadTexts: qbQosIfStatDownThreshDiscPkts.setDescription('A count of the number of downstream packets discarded for this interface due to thresholding on this interface.')
qbQosNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 2, 0))
qbQosCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1))
qbQosGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2))
qbQosCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1, 1)).setObjects(("QB-QOS-MGMT-MIB", "qbQosClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbQosCompliance = qbQosCompliance.setStatus('current')
if mibBuilder.loadTexts: qbQosCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
qbQosGroupInfo = ObjectGroup((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2, 1)).setObjects(("QB-QOS-MGMT-MIB", "qbQosIfConfPolicingAdminStatus"), ("QB-QOS-MGMT-MIB", "qbQosIfStatDiscPkts"), ("QB-QOS-MGMT-MIB", "qbQosIfStatUpThreshDiscPkts"), ("QB-QOS-MGMT-MIB", "qbQosIfStatDownThreshDiscPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbQosGroupInfo = qbQosGroupInfo.setStatus('current')
if mibBuilder.loadTexts: qbQosGroupInfo.setDescription('The set of all accessible objects in this MIB.')
mibBuilder.exportSymbols("QB-QOS-MGMT-MIB", qbQosIfStatEntry=qbQosIfStatEntry, qbQosMIB=qbQosMIB, qbQosIfConfGroup=qbQosIfConfGroup, qbQosIfConfPolicingAdminStatus=qbQosIfConfPolicingAdminStatus, qbQosCompliance=qbQosCompliance, qbQosIfConfEntry=qbQosIfConfEntry, qbQosConformance=qbQosConformance, PYSNMP_MODULE_ID=qbQosMIB, qbQosIfStatDiscPkts=qbQosIfStatDiscPkts, qbQosNotificationPrefix=qbQosNotificationPrefix, qbQosNotifications=qbQosNotifications, qbQosObjects=qbQosObjects, QbMbitRate=QbMbitRate, qbQosIfStatDownThreshDiscPkts=qbQosIfStatDownThreshDiscPkts, qbQosIfConfTable=qbQosIfConfTable, qbQosIfStatUpThreshDiscPkts=qbQosIfStatUpThreshDiscPkts, qbQosGroupInfo=qbQosGroupInfo, qbQosIfStatTable=qbQosIfStatTable, qbQosIfConfTableLastUpdate=qbQosIfConfTableLastUpdate, qbQosCompliances=qbQosCompliances, qbQosGroups=qbQosGroups)
