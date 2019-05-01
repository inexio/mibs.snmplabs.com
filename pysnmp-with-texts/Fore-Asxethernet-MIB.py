#
# PySNMP MIB module Fore-Asxethernet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Asxethernet-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:16:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
software, = mibBuilder.importSymbols("Fore-Common-MIB", "software")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Unsigned32, MibIdentifier, iso, ModuleIdentity, ObjectIdentity, NotificationType, Integer32, IpAddress, Gauge32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Integer32", "IpAddress", "Gauge32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
asxEthernetAutoNegotiate = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5))
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setOrganization('FORE')
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: asxEthernetAutoNegotiate.setDescription('Fore Switch ASX extensions to the etherlike mib.')
class AsxEthernetModes(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("tenHalfDuplex", 1), ("tenFullDuplex", 2), ("hundredHalfDuplex", 3), ("hundredFullDuplex", 4), ("auto", 5))

asxEthernetAutoNegotiationTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: asxEthernetAutoNegotiationTable.setStatus('current')
if mibBuilder.loadTexts: asxEthernetAutoNegotiationTable.setDescription('A table that contains the auto negotiation informtion about every port of a given alchemy blade.')
asxEthernetAutoNegotiationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: asxEthernetAutoNegotiationEntry.setStatus('current')
if mibBuilder.loadTexts: asxEthernetAutoNegotiationEntry.setDescription('A list of auto negotiation information that is maintained per port per blade. The configuration information of the port is also mainatained.')
asxEthernetConfigModes = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 1), AsxEthernetModes()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: asxEthernetConfigModes.setStatus('current')
if mibBuilder.loadTexts: asxEthernetConfigModes.setDescription('The mode which the port should be configured to. The default mode is auto.')
asxEthernetOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 2), AsxEthernetModes()).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetOperStatus.setStatus('current')
if mibBuilder.loadTexts: asxEthernetOperStatus.setDescription('The actual operational mode of this port. Note that the values for this object are invalid if the asxEthernetLinkState is link-down.')
asxEthernetLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetLinkState.setStatus('current')
if mibBuilder.loadTexts: asxEthernetLinkState.setDescription('This object signifies if the link on the specified port is actually up or down')
asxEthernetRemoteAutoNeg = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detected", 1), ("not-detected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetRemoteAutoNeg.setStatus('current')
if mibBuilder.loadTexts: asxEthernetRemoteAutoNeg.setDescription('This object signifies whether the remote end of the link is using auto-negotiation.')
asxEthernetRemoteOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 0), ("tenHalfDuplex", 1), ("tenFullDuplex", 2), ("hundredHalfDuplex", 3), ("hundredFullDuplex", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: asxEthernetRemoteOperStatus.setStatus('current')
if mibBuilder.loadTexts: asxEthernetRemoteOperStatus.setDescription('The actual operational mode of the remote end of this link. The value of this object is invalid if the asxEthernetRemoteAutoNeg is not-detected.')
mibBuilder.exportSymbols("Fore-Asxethernet-MIB", PYSNMP_MODULE_ID=asxEthernetAutoNegotiate, asxEthernetRemoteAutoNeg=asxEthernetRemoteAutoNeg, asxEthernetAutoNegotiate=asxEthernetAutoNegotiate, asxEthernetLinkState=asxEthernetLinkState, asxEthernetAutoNegotiationEntry=asxEthernetAutoNegotiationEntry, asxEthernetRemoteOperStatus=asxEthernetRemoteOperStatus, asxEthernetAutoNegotiationTable=asxEthernetAutoNegotiationTable, asxEthernetConfigModes=asxEthernetConfigModes, AsxEthernetModes=AsxEthernetModes, asxEthernetOperStatus=asxEthernetOperStatus)
