#
# PySNMP MIB module Nortel-Magellan-Passport-StateSummaryMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-StateSummaryMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:28:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
components, passportMIBs = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "components", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, Gauge32, ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, NotificationType, Counter64, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "Counter64", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stateSummaryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7))
if mibBuilder.loadTexts: stateSummaryMIB.setLastUpdated('9707150000Z')
if mibBuilder.loadTexts: stateSummaryMIB.setOrganization('Nortel')
if mibBuilder.loadTexts: stateSummaryMIB.setContactInfo(' Nortel Magellan Network Management Postal: P.O. Box 5080, Station F Ottawa, Ontario Canada K2C 3T1 Email: nm_plm@nt.com')
if mibBuilder.loadTexts: stateSummaryMIB.setDescription('This MIB module specifies the variables used to implement the Nortel Magellan Passport state summary functionality.')
stateSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5))
timeOfLastTableChange = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 1))
timeOfLastStateSummTableChange = MibScalar((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeOfLastStateSummTableChange.setStatus('current')
if mibBuilder.loadTexts: timeOfLastStateSummTableChange.setDescription('The value of sysUpTime at the time that an entry in the compClassTable detected a change.')
compClassTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2), )
if mibBuilder.loadTexts: compClassTable.setStatus('current')
if mibBuilder.loadTexts: compClassTable.setDescription('A list of component classes that have state information summaries.')
compClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-StateSummaryMIB", "compClass"))
if mibBuilder.loadTexts: compClassEntry.setStatus('current')
if mibBuilder.loadTexts: compClassEntry.setDescription('A component class entry.')
compClass = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compClass.setStatus('current')
if mibBuilder.loadTexts: compClass.setDescription('An object identifier which points to the SNMP Mib Arc for that particular component class. For example, a replication of 1.3.6.1.4.1.562.2.4.1.12 (iso.org.dod. internet.private.enterprises.nortel.magellan.passport. components.lp) corresponds to the Lp component class.')
compName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: compName.setStatus('current')
if mibBuilder.loadTexts: compName.setDescription('The string representation of the component class object identifier. For example, 1.3.6.1.4.1.562.2.4.1.12 (iso.org. dod.internet.private.enterprises.nortel.magellan.passport. components.lp) is represented as the string, LogicalProcessor.')
timeOfLastStateStatusChange = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeOfLastStateStatusChange.setStatus('current')
if mibBuilder.loadTexts: timeOfLastStateStatusChange.setDescription('The value of sysUpTime when an OsiState or OsiStateStatus change was detected for the component class. Currently monitored attributes include: AdminState, OperationalState, AvailabilityStatus and AlarmStatus.')
numberDown = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberDown.setStatus('current')
if mibBuilder.loadTexts: numberDown.setDescription('The number of component instances that are down. A component is considered down when its administrative state is locked or its operational state is disabled. ')
numberTroubled = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberTroubled.setStatus('current')
if mibBuilder.loadTexts: numberTroubled.setDescription('The number of component instances that are troubled. A component is considered troubled when its administrative status is shuttingDown or its alarm status is not empty or its availability status is degraded.')
stateSummaryGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7, 1, 3, 2, 2))
stateSummaryCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 7, 3, 3, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-StateSummaryMIB", stateSummaryMIB=stateSummaryMIB, timeOfLastTableChange=timeOfLastTableChange, PYSNMP_MODULE_ID=stateSummaryMIB, stateSummaryCapabilitiesBE00A=stateSummaryCapabilitiesBE00A, stateSummaryGroupBE00A=stateSummaryGroupBE00A, compClassEntry=compClassEntry, stateSummary=stateSummary, timeOfLastStateStatusChange=timeOfLastStateStatusChange, compClass=compClass, timeOfLastStateSummTableChange=timeOfLastStateSummTableChange, compName=compName, numberDown=numberDown, numberTroubled=numberTroubled, compClassTable=compClassTable)
