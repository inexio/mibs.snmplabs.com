#
# PySNMP MIB module ARUBA-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARUBA-MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
arubaMgmt, = mibBuilder.importSymbols("ARUBA-MIB", "arubaMgmt")
ArubaEnableValue, = mibBuilder.importSymbols("ARUBA-TC", "ArubaEnableValue")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, TimeTicks, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, iso, Integer32, Counter32, ModuleIdentity, Unsigned32, Gauge32, MibIdentifier, NotificationType, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "iso", "Integer32", "Counter32", "ModuleIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "ObjectName")
PhysAddress, TruthValue, TextualConvention, TestAndIncr, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TruthValue", "TextualConvention", "TestAndIncr", "TimeStamp", "DisplayString")
arubaMgmtExtensions = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 3, 3))
if mibBuilder.loadTexts: arubaMgmtExtensions.setLastUpdated('0804160206Z')
if mibBuilder.loadTexts: arubaMgmtExtensions.setOrganization('Aruba Wireless Networks')
if mibBuilder.loadTexts: arubaMgmtExtensions.setContactInfo('Postal: 1322 Crossman Avenue Sunnyvale, CA 94089 E-mail: dl-support@arubanetworks.com Phone: +1 408 227 4500')
if mibBuilder.loadTexts: arubaMgmtExtensions.setDescription('A MIB module for supporting the Aruba Management Protocol. This protocol is an extension to SNMP.')
arubaMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1))
arubaGetTable = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: arubaGetTable.setStatus('current')
if mibBuilder.loadTexts: arubaGetTable.setDescription(' The object is used in the Aruba Management Protocol. In a GET Table request the instance of the object will contain the Table/Entry OID to be retrieved. The value of the object in a GET Table response is the table OID or Entry OID. A Get request on this object returns <0.0>. ')
arubaNumberOfRows = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: arubaNumberOfRows.setStatus('current')
if mibBuilder.loadTexts: arubaNumberOfRows.setDescription(' The object is used in the Aruba Management Protocol. This Object is used to specify the number of Objects to be retrieved in a GET Table request. Instance of the Object will contain the number of Rows. In the Response to the GET Table this object will contain the number of Objects returned in the response. A Get request on this object returns 0. ')
arubaRowInstance = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: arubaRowInstance.setStatus('current')
if mibBuilder.loadTexts: arubaRowInstance.setDescription(' The object is used in the Aruba Management Protocol. This Object is used to specify the Row Instance in the GET Table Request. The response will start from the Next Row. Instance of the Object is the row instance of the request. In the Response to the GET Table this object will contain the Instance of Last row included in the response. A Get request on this object returns <0.0> . ')
arubaGetTableStatus = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("endTable", 1), ("moreTable", 2), ("retrieveError", 3), ("noAmpSupport", 4), ("invalidColumnID", 5), ("resourceAllocationFailure", 6))))
if mibBuilder.loadTexts: arubaGetTableStatus.setStatus('current')
if mibBuilder.loadTexts: arubaGetTableStatus.setDescription(' The object is used in the Aruba Management Protocol. This Object is used to give the status of the GetTable request. endTable -- indicates that there are no more rows in the table. moreTable -- indicates that there are some more rows in the table. retrieveError -- indicates an error occurred while processing the getTable request. (Will be expanded ). A Get request on this object returns 0 . ')
arubaNumberOfColumns = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 5), Integer32())
if mibBuilder.loadTexts: arubaNumberOfColumns.setStatus('current')
if mibBuilder.loadTexts: arubaNumberOfColumns.setDescription(' The object is used in the Aruba Management Protocol. This Object is used to specify the number of Columns per row in the Get Table Response. A Get request on this object returns 0. ')
arubaSwitchAMPSupport = MibScalar((1, 3, 6, 1, 4, 1, 14823, 3, 3, 1, 6), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: arubaSwitchAMPSupport.setStatus('current')
if mibBuilder.loadTexts: arubaSwitchAMPSupport.setDescription(' The object is used in the Aruba Management Protocol. This Object is used to specify the number of Columns per row in the Get Table Response. A Get request on this object returns 0. ')
mibBuilder.exportSymbols("ARUBA-MGMT-MIB", arubaMgmtExtensions=arubaMgmtExtensions, arubaNumberOfRows=arubaNumberOfRows, PYSNMP_MODULE_ID=arubaMgmtExtensions, arubaGetTableStatus=arubaGetTableStatus, arubaNumberOfColumns=arubaNumberOfColumns, arubaSwitchAMPSupport=arubaSwitchAMPSupport, arubaRowInstance=arubaRowInstance, arubaMgmtGroup=arubaMgmtGroup, arubaGetTable=arubaGetTable)
