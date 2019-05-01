#
# PySNMP MIB module ZYXEL-OUT-OF-BAND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-OUT-OF-BAND-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:51:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, NotificationType, iso, MibIdentifier, Counter32, Unsigned32, Gauge32, IpAddress, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "MibIdentifier", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelOutOfBand = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58))
if mibBuilder.loadTexts: zyxelOutOfBand.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelOutOfBand.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelOutOfBand.setContactInfo('')
if mibBuilder.loadTexts: zyxelOutOfBand.setDescription('The subtree for out-of-band management IP address')
zyxelOutOfBandIpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1))
zyOutOfBandIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyOutOfBandIpAddress.setDescription('Enter the out-of-band management IP address of your switch in dotted decimal notation. For example, 192.168.0.1.')
zyOutOfBandSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandSubnetMask.setStatus('current')
if mibBuilder.loadTexts: zyOutOfBandSubnetMask.setDescription('Enter the IP subnet mask of your switch in dotted decimal notation, for example, 255.255.255.0.')
zyOutOfBandGateway = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 58, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyOutOfBandGateway.setStatus('current')
if mibBuilder.loadTexts: zyOutOfBandGateway.setDescription('Enter the IP address of the default outgoing gateway in dotted decimal notation, for example, 192.168.0.254.')
mibBuilder.exportSymbols("ZYXEL-OUT-OF-BAND-MIB", zyxelOutOfBandIpSetup=zyxelOutOfBandIpSetup, zyOutOfBandSubnetMask=zyOutOfBandSubnetMask, zyOutOfBandGateway=zyOutOfBandGateway, zyxelOutOfBand=zyxelOutOfBand, PYSNMP_MODULE_ID=zyxelOutOfBand, zyOutOfBandIpAddress=zyOutOfBandIpAddress)
