#
# PySNMP MIB module HUAWEI-8040IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-8040IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
mlsr, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "mlsr")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, Unsigned32, TimeTicks, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, ModuleIdentity, Counter64, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "ModuleIdentity", "Counter64", "iso", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hw8040If = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7))
if mibBuilder.loadTexts: hw8040If.setLastUpdated('200410110000Z')
if mibBuilder.loadTexts: hw8040If.setOrganization('Huawei-3com Technologies co.,Ltd.')
if mibBuilder.loadTexts: hw8040If.setContactInfo('Platform Team Beijing Institute Huawei-3com Tech, Inc. Http://www.huawei-3com.com E-mail:support@huawei-3com.com ')
if mibBuilder.loadTexts: hw8040If.setDescription(' ')
hw8040IfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1), )
if mibBuilder.loadTexts: hw8040IfTable.setStatus('current')
if mibBuilder.loadTexts: hw8040IfTable.setDescription('The table describles the private attributes of Quidway router. ')
hw8040IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hw8040IfEntry.setStatus('current')
if mibBuilder.loadTexts: hw8040IfEntry.setDescription('Each entry contains the attributes associated with a Quidway router entity.')
hw8040IfInPerSecBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfInPerSecBits.setStatus('current')
if mibBuilder.loadTexts: hw8040IfInPerSecBits.setDescription(' The 5 minutes exponentially-decayed moving average of bits per second input from the interface . ')
hw8040IfOutPerSecBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfOutPerSecBits.setStatus('current')
if mibBuilder.loadTexts: hw8040IfOutPerSecBits.setDescription(' The 5 minutes exponentially-decayed moving average of bits per second output from the interface . ')
hw8040CRCIfInputErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040CRCIfInputErr.setStatus('current')
if mibBuilder.loadTexts: hw8040CRCIfInputErr.setDescription(' The statistics of CRC errors of input packets of the interface.')
hw8040IfOutCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hw8040IfOutCollisions.setStatus('current')
if mibBuilder.loadTexts: hw8040IfOutCollisions.setDescription(' The statistics of collision numbers of output which are detected on the interface.')
hw8040IfDescCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hw8040IfDescCfg.setStatus('current')
if mibBuilder.loadTexts: hw8040IfDescCfg.setDescription('The description of the interface which is user configurable .')
mibBuilder.exportSymbols("HUAWEI-8040IF-MIB", hw8040If=hw8040If, hw8040IfOutPerSecBits=hw8040IfOutPerSecBits, hw8040IfEntry=hw8040IfEntry, hw8040IfDescCfg=hw8040IfDescCfg, hw8040IfInPerSecBits=hw8040IfInPerSecBits, hw8040IfTable=hw8040IfTable, hw8040CRCIfInputErr=hw8040CRCIfInputErr, hw8040IfOutCollisions=hw8040IfOutCollisions, PYSNMP_MODULE_ID=hw8040If)