#
# PySNMP MIB module MERU-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-SMI
# Produced by pysmi-0.3.4 at Wed May  1 14:11:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter32, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, IpAddress, ObjectIdentity, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
meru = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983))
if mibBuilder.loadTexts: meru.setLastUpdated('200504250000Z')
if mibBuilder.loadTexts: meru.setOrganization('Meru Networks')
if mibBuilder.loadTexts: meru.setContactInfo('support@merunetworks.com')
if mibBuilder.loadTexts: meru.setDescription('The Structure of Management Information for the Meru enterprise. All Meru MIBs are located under this subtree.')
meru_reg = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1)).setLabel("meru-reg")
meru_wlan = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1)).setLabel("meru-wlan")
meru_modules = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 2)).setLabel("meru-modules")
mwStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 3))
if mibBuilder.loadTexts: mwStatistics.setStatus('current')
if mibBuilder.loadTexts: mwStatistics.setDescription('Wlan Statisstics')
mwConfiguration = ObjectIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4))
if mibBuilder.loadTexts: mwConfiguration.setStatus('current')
if mibBuilder.loadTexts: mwConfiguration.setDescription('Wlan system configuration')
mwDiagnostics = ObjectIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 5))
if mibBuilder.loadTexts: mwDiagnostics.setStatus('current')
if mibBuilder.loadTexts: mwDiagnostics.setDescription('Wlan system monitoring')
meruAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 6))
if mibBuilder.loadTexts: meruAgentCapability.setStatus('current')
if mibBuilder.loadTexts: meruAgentCapability.setDescription('Meru agent capability')
mwControllers = ObjectIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7))
if mibBuilder.loadTexts: mwControllers.setStatus('current')
if mibBuilder.loadTexts: mwControllers.setDescription('This object defines identity of mobility and wireless controllers.')
mc500 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 1))
mc1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 2))
mc1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 3))
mc3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 4))
mc500a = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 5))
mc5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 6))
mc4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 7))
mc4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 8))
mc1500 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 9))
mc3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 10))
mc4200 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 11))
mc6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 12))
mc1500v = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 13))
mc3200v = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 14))
mc4200v = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 15))
mc1550 = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 16))
mc1550v = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 7, 17))
mibBuilder.exportSymbols("MERU-SMI", mc1550=mc1550, meru_modules=meru_modules, mc4200v=mc4200v, meru_reg=meru_reg, mc3000=mc3000, mc1500v=mc1500v, mc6000=mc6000, mwConfiguration=mwConfiguration, meru=meru, mc500a=mc500a, mc5000=mc5000, mc500=mc500, mc1550v=mc1550v, mc1500=mc1500, mc4100=mc4100, mc1000=mc1000, meruAgentCapability=meruAgentCapability, mc3200v=mc3200v, mc4000=mc4000, mc3200=mc3200, PYSNMP_MODULE_ID=meru, mwControllers=mwControllers, meru_wlan=meru_wlan, mwDiagnostics=mwDiagnostics, mc4200=mc4200, mc1100=mc1100, mwStatistics=mwStatistics)
