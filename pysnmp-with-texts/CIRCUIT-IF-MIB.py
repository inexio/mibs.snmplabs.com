#
# PySNMP MIB module CIRCUIT-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIRCUIT-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Bits, iso, Counter64, MibIdentifier, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "iso", "Counter64", "MibIdentifier", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "mib-2")
RowStatus, RowPointer, TimeStamp, StorageType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "RowPointer", "TimeStamp", "StorageType", "TextualConvention", "DisplayString")
circuitIfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 94))
circuitIfMIB.setRevisions(('2002-01-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: circuitIfMIB.setRevisionsDescriptions(('Initial version, published as RFC 3201',))
if mibBuilder.loadTexts: circuitIfMIB.setLastUpdated('200201030000Z')
if mibBuilder.loadTexts: circuitIfMIB.setOrganization('IETF Frame Relay Service MIB Working Group')
if mibBuilder.loadTexts: circuitIfMIB.setContactInfo('IETF Frame Relay Service MIB (frnetmib) Working Group WG Charter: http://www.ietf.org/html.charters/ frnetmib-charter.html WG-email: frnetmib@sunroof.eng.sun.com Subscribe: frnetmib-request@sunroof.eng.sun.com Email Archive: ftp://ftp.ietf.org/ietf-mail-archive/frnetmib Chair: Andy Malis Vivace Networks Email: Andy.Malis@vivacenetworks.com WG editor: Robert Steinberger Paradyne Networks and Fujitsu Network Communications Email: robert.steinberger@fnc.fujitsu.com Co-author: Orly Nicklass RAD Data Communications Ltd. EMail: Orly_n@rad.co.il')
if mibBuilder.loadTexts: circuitIfMIB.setDescription('The MIB module to allow insertion of selected circuit into the ifTable.')
class CiFlowDirection(TextualConvention, Integer32):
    description = 'The direction of data flow thru a circuit. transmit(1) - Only transmitted data receive(2) - Only received data both(3) - Both transmitted and received data.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("transmit", 1), ("receive", 2), ("both", 3))

ciObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 1))
ciCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 2))
ciConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3))
ciCircuitTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 1), )
if mibBuilder.loadTexts: ciCircuitTable.setStatus('current')
if mibBuilder.loadTexts: ciCircuitTable.setDescription('The Circuit Interface Circuit Table.')
ciCircuitEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 1, 1), ).setIndexNames((0, "CIRCUIT-IF-MIB", "ciCircuitObject"), (0, "CIRCUIT-IF-MIB", "ciCircuitFlow"))
if mibBuilder.loadTexts: ciCircuitEntry.setStatus('current')
if mibBuilder.loadTexts: ciCircuitEntry.setDescription('An entry in the Circuit Interface Circuit Table.')
ciCircuitObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 1), RowPointer())
if mibBuilder.loadTexts: ciCircuitObject.setStatus('current')
if mibBuilder.loadTexts: ciCircuitObject.setDescription('This value contains the RowPointer that uniquely describes the circuit that is to be added to this table. Any RowPointer that will force the size of OBJECT IDENTIFIER of the row to grow beyond the legal limit MUST be rejected. The purpose of this object is to point a network manager to the table in which the circuit was created as well as define the circuit on which the interface is defined. Valid tables for this object include the frCircuitTable from the Frame Relay DTE MIB(FRAME-RELAY-DTE-MIB), the frPVCEndptTable from the Frame Relay Service MIB (FRNETSERV-MIB), and the aal5VccTable from the ATM MIB (ATM MIB). However, including circuits from other MIB tables IS NOT prohibited.')
ciCircuitFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 2), CiFlowDirection())
if mibBuilder.loadTexts: ciCircuitFlow.setStatus('current')
if mibBuilder.loadTexts: ciCircuitFlow.setDescription('The direction of data flow through the circuit for which the virtual interface is defined. The following define the information that the virtual interface will report. transmit(1) - Only transmitted frames receive(2) - Only received frames both(3) - Both transmitted and received frames. It is recommended that the ifDescr of the circuit interfaces that are not both(3) SHOULD have text warning the operators that the particular interface represents only half the traffic on the circuit.')
ciCircuitStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciCircuitStatus.setStatus('current')
if mibBuilder.loadTexts: ciCircuitStatus.setDescription('The status of the current row. This object is used to add, delete, and disable rows in this table. When the status changes to active(1), a row will also be added to the interface map table below and a row will be added to the ifTable. These rows SHOULD not be removed until the status is changed from active(1). The value of ifIndex for the row that is added to the ifTable is determined by the agent and MUST follow the rules of the ifTable. The value of ifType for that interface will be frDlciEndPt(193) for a frame relay circuit, atmVciEndPt(194) for an ATM circuit, or another ifType defining the circuit type for any other circuit. When this object is set to destroy(6), the associated row in the interface map table will be removed and the ifIndex will be removed from the ifTable. Removing the ifIndex MAY initiate a chain of events that causes changes to other tables as well. The rows added to this table MUST have a valid object identifier for ciCircuitObject. This means that the referenced object must exist and it must be in a table that supports circuits. The object referenced by ciCircuitObject MUST exist prior to transitioning a row to active(1). If at any point the object referenced by ciCircuitObject does not exist or the row containing it is not in the active(1) state, the status SHOULD either age out the row or report notReady(3). The effects transitioning from active(1) to notReady(3) are the same as those caused by setting the status to destroy(6). Each row in this table relies on information from other MIB modules. The rules persistence of data SHOULD follow the same rules as those of the underlying MIB module. For example, if the circuit defined by ciCircuitObject would normally be stored in non-volatile memory, then the row SHOULD also be non-volatile.')
ciCircuitIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciCircuitIfIndex.setStatus('current')
if mibBuilder.loadTexts: ciCircuitIfIndex.setDescription('The ifIndex that the agent assigns to this row.')
ciCircuitCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciCircuitCreateTime.setStatus('current')
if mibBuilder.loadTexts: ciCircuitCreateTime.setDescription('This object returns the value of sysUpTime at the time the value of ciCircuitStatus last transitioned to active(1). If ciCircuitStatus has never been active(1), this object SHOULD return 0.')
ciCircuitStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciCircuitStorageType.setStatus('current')
if mibBuilder.loadTexts: ciCircuitStorageType.setDescription('The storage type used for this row.')
ciIfMapTable = MibTable((1, 3, 6, 1, 2, 1, 94, 1, 2), )
if mibBuilder.loadTexts: ciIfMapTable.setStatus('current')
if mibBuilder.loadTexts: ciIfMapTable.setDescription('The Circuit Interface Map Table.')
ciIfMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 94, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ciIfMapEntry.setStatus('current')
if mibBuilder.loadTexts: ciIfMapEntry.setDescription('An entry in the Circuit Interface Map Table.')
ciIfMapObject = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 1), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfMapObject.setStatus('current')
if mibBuilder.loadTexts: ciIfMapObject.setDescription('This value contains the value of RowPointer that corresponds to the current ifIndex.')
ciIfMapFlow = MibTableColumn((1, 3, 6, 1, 2, 1, 94, 1, 2, 1, 2), CiFlowDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfMapFlow.setStatus('current')
if mibBuilder.loadTexts: ciIfMapFlow.setDescription('The value contains the value of ciCircuitFlow that corresponds to the current ifIndex.')
ciIfLastChange = MibScalar((1, 3, 6, 1, 2, 1, 94, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfLastChange.setStatus('current')
if mibBuilder.loadTexts: ciIfLastChange.setDescription('The value of sysUpTime at the most recent change to ciCircuitStatus for any row in ciCircuitTable.')
ciIfNumActive = MibScalar((1, 3, 6, 1, 2, 1, 94, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciIfNumActive.setStatus('current')
if mibBuilder.loadTexts: ciIfNumActive.setDescription('The number of active rows in ciCircuitTable.')
ciMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 1))
ciMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 94, 3, 2))
ciCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 94, 3, 2, 1)).setObjects(("CIRCUIT-IF-MIB", "ciCircuitGroup"), ("CIRCUIT-IF-MIB", "ciIfMapGroup"), ("CIRCUIT-IF-MIB", "ciStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciCompliance = ciCompliance.setStatus('current')
if mibBuilder.loadTexts: ciCompliance.setDescription('The compliance statement for SNMP entities which support of the Circuit Interfaces MIB module. This group defines the minimum level of support required for compliance.')
ciCircuitGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 1)).setObjects(("CIRCUIT-IF-MIB", "ciCircuitStatus"), ("CIRCUIT-IF-MIB", "ciCircuitIfIndex"), ("CIRCUIT-IF-MIB", "ciCircuitCreateTime"), ("CIRCUIT-IF-MIB", "ciCircuitStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciCircuitGroup = ciCircuitGroup.setStatus('current')
if mibBuilder.loadTexts: ciCircuitGroup.setDescription('A collection of required objects providing information from the circuit table.')
ciIfMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 2)).setObjects(("CIRCUIT-IF-MIB", "ciIfMapObject"), ("CIRCUIT-IF-MIB", "ciIfMapFlow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciIfMapGroup = ciIfMapGroup.setStatus('current')
if mibBuilder.loadTexts: ciIfMapGroup.setDescription('A collection of required objects providing information from the interface map table.')
ciStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 94, 3, 1, 3)).setObjects(("CIRCUIT-IF-MIB", "ciIfLastChange"), ("CIRCUIT-IF-MIB", "ciIfNumActive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciStatsGroup = ciStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciStatsGroup.setDescription('A collection of statistical metrics used to help manage the ciCircuitTable.')
mibBuilder.exportSymbols("CIRCUIT-IF-MIB", ciMIBGroups=ciMIBGroups, ciIfMapTable=ciIfMapTable, ciIfMapObject=ciIfMapObject, PYSNMP_MODULE_ID=circuitIfMIB, ciCircuitTable=ciCircuitTable, ciCircuitStorageType=ciCircuitStorageType, ciIfMapEntry=ciIfMapEntry, ciCircuitCreateTime=ciCircuitCreateTime, ciCompliance=ciCompliance, ciCapabilities=ciCapabilities, ciCircuitIfIndex=ciCircuitIfIndex, ciObjects=ciObjects, ciIfLastChange=ciIfLastChange, ciConformance=ciConformance, ciStatsGroup=ciStatsGroup, ciCircuitFlow=ciCircuitFlow, ciIfNumActive=ciIfNumActive, ciCircuitEntry=ciCircuitEntry, circuitIfMIB=circuitIfMIB, ciCircuitObject=ciCircuitObject, ciCircuitStatus=ciCircuitStatus, ciCircuitGroup=ciCircuitGroup, CiFlowDirection=CiFlowDirection, ciMIBCompliances=ciMIBCompliances, ciIfMapFlow=ciIfMapFlow, ciIfMapGroup=ciIfMapGroup)
