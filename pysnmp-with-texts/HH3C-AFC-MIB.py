#
# PySNMP MIB module HH3C-AFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-AFC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, Gauge32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier, iso, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "Gauge32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cAFC = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 85))
hh3cAFC.setRevisions(('2008-07-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cAFC.setRevisionsDescriptions(('The Initial Version of this MIB module.',))
if mibBuilder.loadTexts: hh3cAFC.setLastUpdated('200807230000Z')
if mibBuilder.loadTexts: hh3cAFC.setOrganization('HH3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cAFC.setContactInfo('PLAT Team Hangzhou HH3C Technologies Co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.hh3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cAFC.setDescription('This MIB is to provide the definition of Abnormal Flow Clean system.')
hh3cAFCLeaf = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1))
hh3cDDosAttackTargetIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 1), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDDosAttackTargetIP.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackTargetIP.setDescription('This shows the victim of a DDos attack. The IP Address is in the list of protected IP address.')
hh3cDDosAttackType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 18, 19, 20, 24, 27, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 1024))).clone(namedValues=NamedValues(("land", 1), ("smurf", 2), ("fraggle", 3), ("winnuke", 4), ("synflood", 5), ("icmpflood", 6), ("udpflood", 7), ("icmpredirect", 8), ("icmpunreachable", 9), ("tracert", 11), ("tcpflag", 12), ("pingofdeath", 13), ("teardrop", 14), ("ipfragment", 15), ("largeicmp", 18), ("sourceroute", 19), ("routerecord", 20), ("fragflood", 24), ("scan", 27), ("appstreamalarm", 29), ("sessionstreamalarm", 30), ("tcpabnormal", 32), ("ipfragabnormal", 33), ("tftpabnormal", 34), ("dnsabnormal", 35), ("httpabnormal", 36), ("telnetabnormal", 37), ("ftpabnormal", 38), ("smtpabnormal", 39), ("pop3abnormal", 40), ("snmpabnormal", 41), ("ackabnormal", 42), ("cc", 43), ("otherabnormal", 1024)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDDosAttackType.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackType.setDescription('This shows the attack type which the victim is sufferd.')
hh3cDDosAttackPolicy = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDDosAttackPolicy.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackPolicy.setDescription('This shows the policy name which detects the DDos Attack.')
hh3cDDosAttackThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDDosAttackThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackThreshold.setDescription('This shows the policy threshold in the DDos Attack.')
hh3cDDosAttackSpeed = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 85, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDDosAttackSpeed.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackSpeed.setDescription('This shows the rate of policy in the DDos Attack.')
hh3cAFCNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 85, 2))
hh3cAFCNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0))
hh3cDDosAttackStart = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 1)).setObjects(("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP"), ("HH3C-AFC-MIB", "hh3cDDosAttackType"), ("HH3C-AFC-MIB", "hh3cDDosAttackPolicy"), ("HH3C-AFC-MIB", "hh3cDDosAttackThreshold"), ("HH3C-AFC-MIB", "hh3cDDosAttackSpeed"))
if mibBuilder.loadTexts: hh3cDDosAttackStart.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackStart.setDescription('This trap is sent when a DDos attack on specific IP is detected. The IP address of the victim is the first object. The exact type of the attack is the second object. The policy name which detects the attack is the third object. The threshold of the attack is the 4th object. The speed of the attack is the 5th object.')
hh3cDDosAttackEnd = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 85, 2, 0, 2)).setObjects(("HH3C-AFC-MIB", "hh3cDDosAttackTargetIP"))
if mibBuilder.loadTexts: hh3cDDosAttackEnd.setStatus('current')
if mibBuilder.loadTexts: hh3cDDosAttackEnd.setDescription('This trap is sent when a DDos Attack end. The IP address of the victim is the very object.')
mibBuilder.exportSymbols("HH3C-AFC-MIB", hh3cAFCNotifyPrefix=hh3cAFCNotifyPrefix, hh3cAFC=hh3cAFC, hh3cDDosAttackType=hh3cDDosAttackType, hh3cDDosAttackTargetIP=hh3cDDosAttackTargetIP, hh3cDDosAttackStart=hh3cDDosAttackStart, hh3cDDosAttackThreshold=hh3cDDosAttackThreshold, hh3cDDosAttackPolicy=hh3cDDosAttackPolicy, hh3cDDosAttackEnd=hh3cDDosAttackEnd, hh3cDDosAttackSpeed=hh3cDDosAttackSpeed, PYSNMP_MODULE_ID=hh3cAFC, hh3cAFCLeaf=hh3cAFCLeaf, hh3cAFCNotify=hh3cAFCNotify)
