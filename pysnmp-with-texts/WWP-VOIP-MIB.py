#
# PySNMP MIB module WWP-VOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-VOIP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Integer32, ModuleIdentity, Bits, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, ObjectIdentity, Counter64, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Integer32", "ModuleIdentity", "Bits", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "MibIdentifier", "Unsigned32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpVoipMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 15))
wwpVoipMIB.setRevisions(('2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpVoipMIB.setRevisionsDescriptions(('Initial creation.',))
if mibBuilder.loadTexts: wwpVoipMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpVoipMIB.setOrganization('World Wide Packets, Inc')
if mibBuilder.loadTexts: wwpVoipMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpVoipMIB.setDescription('This MIB module is for Voice Over IP feature on WWP Products')
wwpVoipMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1))
wwpVoip = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1))
wwpVoipMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2))
wwpVoipMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0))
wwpVoipMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3))
wwpVoipMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 1))
wwpVoipMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 15, 3, 2))
wwpVoipTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1), )
if mibBuilder.loadTexts: wwpVoipTable.setStatus('current')
if mibBuilder.loadTexts: wwpVoipTable.setDescription('The conceptual table listing all the Voice Over Ip Entries.')
wwpVoipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1), ).setIndexNames((0, "WWP-VOIP-MIB", "wwpVoipIndex"))
if mibBuilder.loadTexts: wwpVoipEntry.setStatus('current')
if mibBuilder.loadTexts: wwpVoipEntry.setDescription('An entry in the wwpVoipTable.')
wwpVoipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipIndex.setStatus('current')
if mibBuilder.loadTexts: wwpVoipIndex.setDescription('Index for the the Voip Entry.')
wwpVoipDownLoaderVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipDownLoaderVersion.setStatus('current')
if mibBuilder.loadTexts: wwpVoipDownLoaderVersion.setDescription('The Downloader version for this VOIP entry.')
wwpVoipApplicationVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipApplicationVersion.setStatus('current')
if mibBuilder.loadTexts: wwpVoipApplicationVersion.setDescription('The Aplication version for this VOIP entry.')
wwpVoipPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipPortNum.setStatus('current')
if mibBuilder.loadTexts: wwpVoipPortNum.setDescription('The Port Number for the VOIP.')
wwpVoipIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipIpAddr.setStatus('current')
if mibBuilder.loadTexts: wwpVoipIpAddr.setDescription('The IP Address for the VOIP Entry.')
wwpVoipNumResets = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipNumResets.setStatus('current')
if mibBuilder.loadTexts: wwpVoipNumResets.setDescription('The number of times the VOIP processor has been reset.')
wwpVoipCallAgentAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpVoipCallAgentAddr.setStatus('current')
if mibBuilder.loadTexts: wwpVoipCallAgentAddr.setDescription('The IP address of the call agent to which this VOIP aplication is connected to.')
wwpVoipResetOp = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 15, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpVoipResetOp.setStatus('current')
if mibBuilder.loadTexts: wwpVoipResetOp.setDescription("This object reset the VOIP Aplication. A read on this object always returns 'none'.")
wwpVoipDiagFailNotification = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 15, 2, 0, 1))
if mibBuilder.loadTexts: wwpVoipDiagFailNotification.setStatus('current')
if mibBuilder.loadTexts: wwpVoipDiagFailNotification.setDescription('A wwpVoipDiagFailNotification is sent if T2 VOIP ASIC fails diagnostics.')
mibBuilder.exportSymbols("WWP-VOIP-MIB", wwpVoipTable=wwpVoipTable, wwpVoipCallAgentAddr=wwpVoipCallAgentAddr, wwpVoipDownLoaderVersion=wwpVoipDownLoaderVersion, wwpVoipMIBCompliances=wwpVoipMIBCompliances, wwpVoipApplicationVersion=wwpVoipApplicationVersion, wwpVoipPortNum=wwpVoipPortNum, wwpVoipResetOp=wwpVoipResetOp, wwpVoipIndex=wwpVoipIndex, wwpVoipEntry=wwpVoipEntry, wwpVoipMIBNotificationPrefix=wwpVoipMIBNotificationPrefix, wwpVoipMIBConformance=wwpVoipMIBConformance, wwpVoipNumResets=wwpVoipNumResets, wwpVoipMIBNotifications=wwpVoipMIBNotifications, wwpVoipMIB=wwpVoipMIB, wwpVoipMIBObjects=wwpVoipMIBObjects, wwpVoip=wwpVoip, wwpVoipIpAddr=wwpVoipIpAddr, wwpVoipDiagFailNotification=wwpVoipDiagFailNotification, wwpVoipMIBGroups=wwpVoipMIBGroups, PYSNMP_MODULE_ID=wwpVoipMIB)
