#
# PySNMP MIB module CXMLPPP-IP-NCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXMLPPP-IP-NCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
cxMLPPP, SapIndex = mibBuilder.importSymbols("CXProduct-SMI", "cxMLPPP", "SapIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, IpAddress, TimeTicks, Counter64, ModuleIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "IpAddress", "TimeTicks", "Counter64", "ModuleIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mlpppIpNsTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52), )
if mibBuilder.loadTexts: mlpppIpNsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsTable.setDescription('A table containing status parameters about each MLPPP module layer PPP IP Network Control Protocol.')
mlpppIpNsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1), ).setIndexNames((0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNsLSapNumber"), (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNsNumber"))
if mibBuilder.loadTexts: mlpppIpNsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsEntry.setDescription('Status parameters for a specific PPP IP Network Control Protocol.')
mlpppIpNsLSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNsLSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsLSapNumber.setDescription('Indicates the row that contains objects for monitoring a SAP that is associated with one of the PPP links. Range of Values: 1-10 Default Value: none')
mlpppIpNsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNsNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsNumber.setDescription('Indicates the row that contains objects for monitoring a SAP that is associated with one of the PPP links. Range of Values: 1 Default Value: none')
mlpppIpNsLocalToRemoteComp = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("vj-tcp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNsLocalToRemoteComp.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsLocalToRemoteComp.setDescription("Identifies whether the local end of the IP-PPP link is using TCP/IP header compression (vj-tcp) to send packets to the remote. The value of this object is determined when the PPP configuration is negotiated. The local port's preference for header compression is determined using mlpppIpNcComp of mlpppIpNcTable. Options: none (1) vj-tcp (2): header compression Default Value: None")
mlpppIpNsRemoteToLocalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 52, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("vj-tcp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNsRemoteToLocalComp.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNsRemoteToLocalComp.setDescription("Identifies whether the remote end of the IP-PPP link is using TCP/IP header compression (vj-tcp) to send packets to the local end. The value of this object is determined when the PPP configuration is negotiated. The local port's preference for header compression is determined using mlpppIpNcComp of mlpppIpNcTable. Options: none (1) vj-tcp (2): header compression Default value: None")
mlpppIpNcTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53), )
if mibBuilder.loadTexts: mlpppIpNcTable.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNcTable.setDescription("A table containing configuration parameters about each MLPPP module layer's PPP IP Network Control Protocol.")
mlpppIpNcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1), ).setIndexNames((0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNcUSapNumber"), (0, "CXMLPPP-IP-NCP-MIB", "mlpppIpNcNumber"))
if mibBuilder.loadTexts: mlpppIpNcEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNcEntry.setDescription('The configuration parameters for a specific PPP IP Network Control Protocol.')
mlpppIpNcUSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNcUSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNcUSapNumber.setDescription('Indicates the row containing objects for monitoring a SAP that is associated with one of the MLPPP links . Range of Values: 1-10 Default Value: none')
mlpppIpNcNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mlpppIpNcNumber.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNcNumber.setDescription('Indicates the row containing objects for monitoring a SAP associated with one of the MLPPP links. Range of Values: 1 Default Value: none')
mlpppIpNcComp = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 49, 53, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("vj-tcp", 2))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mlpppIpNcComp.setReference('Section 4.0, Van Jacobson TCP/IP Header Compression of RFC1332.')
if mibBuilder.loadTexts: mlpppIpNcComp.setStatus('mandatory')
if mibBuilder.loadTexts: mlpppIpNcComp.setDescription('Determines whether the local end of PPP link wants to use TCP/IP header compression (vj-tcp) to send packets over the link. If header compression is desired, the local will negotiate for its implementation with the remote end of the link. The result of the negotiation is displayed in mlpppIpNsLocalToRemoteComp (the local) and mlpppIpNsRemoteToLocalComp (remote). If compression is not desired, there will be no attempt to negotiate with the other end of the link. Options: none (1) vj-tcp (2): header compression Default Value: none Configuration Changed: administrative')
mibBuilder.exportSymbols("CXMLPPP-IP-NCP-MIB", mlpppIpNsRemoteToLocalComp=mlpppIpNsRemoteToLocalComp, mlpppIpNcNumber=mlpppIpNcNumber, mlpppIpNsTable=mlpppIpNsTable, mlpppIpNcEntry=mlpppIpNcEntry, mlpppIpNsNumber=mlpppIpNsNumber, mlpppIpNsLocalToRemoteComp=mlpppIpNsLocalToRemoteComp, mlpppIpNcTable=mlpppIpNcTable, mlpppIpNsLSapNumber=mlpppIpNsLSapNumber, mlpppIpNcUSapNumber=mlpppIpNcUSapNumber, mlpppIpNsEntry=mlpppIpNsEntry, mlpppIpNcComp=mlpppIpNcComp)
