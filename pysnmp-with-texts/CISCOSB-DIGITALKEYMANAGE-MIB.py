#
# PySNMP MIB module CISCOSB-DIGITALKEYMANAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-DIGITALKEYMANAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:22:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, IpAddress, iso, Unsigned32, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "NotificationType")
DateAndTime, DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
rlDigitalKeyManage = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86))
rlDigitalKeyManage.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlDigitalKeyManage.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlDigitalKeyManage.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlDigitalKeyManage.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rlDigitalKeyManage.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDigitalKeyManage.setDescription('This private MIB module defines digital key manage private MIBs.')
rlMD5KeyChainTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1), )
if mibBuilder.loadTexts: rlMD5KeyChainTable.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainTable.setDescription('Key-chains and keys')
rlMD5KeyChainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1), ).setIndexNames((0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainName"), (0, "CISCOSB-DIGITALKEYMANAGE-MIB", "rlMD5KeyChainKeyId"))
if mibBuilder.loadTexts: rlMD5KeyChainEntry.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainEntry.setDescription('Key-chain with key ID that belongs to this chain')
rlMD5KeyChainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMD5KeyChainName.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainName.setDescription('Name of the key-chain to which belongs the secret authentication key')
rlMD5KeyChainKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMD5KeyChainKeyId.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyId.setDescription('A 8-bit identifier for the secret authentication key. This identifier unique only for specific key chain')
rlMD5KeyChainKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainKey.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKey.setDescription('The 128-bit secret authentication key')
rlMD5KeyChainKeyStartAccept = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 4), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainKeyStartAccept.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyStartAccept.setDescription('The time that the router will start accepting packets that have been created with the given key')
rlMD5KeyChainKeyStartGenerate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 5), DateAndTime().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainKeyStartGenerate.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyStartGenerate.setDescription('The time that the router will start using the key for packet generation')
rlMD5KeyChainKeyStopGenerate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 6), DateAndTime().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainKeyStopGenerate.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyStopGenerate.setDescription('The time that the router will stop using the key for packet generation')
rlMD5KeyChainKeyStopAccept = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 7), DateAndTime().clone(hexValue="FFFFFFFF")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainKeyStopAccept.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyStopAccept.setDescription('The time that the router will stop accepting packets that have been created with the given key')
rlMD5KeyChainKeyValidForAccept = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMD5KeyChainKeyValidForAccept.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyValidForAccept.setDescription("A value of 'true' indicates that given key is valid for accepting packets")
rlMD5KeyChainKeyValidForGenerate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMD5KeyChainKeyValidForGenerate.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainKeyValidForGenerate.setDescription("A value of 'true' indicates that given key is valid for packet generation")
rlMD5KeyChainRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 86, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMD5KeyChainRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlMD5KeyChainRowStatus.setDescription('It is used to insert, update or delete an entry')
mibBuilder.exportSymbols("CISCOSB-DIGITALKEYMANAGE-MIB", rlMD5KeyChainKeyStartAccept=rlMD5KeyChainKeyStartAccept, rlMD5KeyChainRowStatus=rlMD5KeyChainRowStatus, rlMD5KeyChainKeyStopGenerate=rlMD5KeyChainKeyStopGenerate, rlMD5KeyChainName=rlMD5KeyChainName, rlMD5KeyChainKeyStartGenerate=rlMD5KeyChainKeyStartGenerate, rlDigitalKeyManage=rlDigitalKeyManage, rlMD5KeyChainKey=rlMD5KeyChainKey, rlMD5KeyChainKeyId=rlMD5KeyChainKeyId, rlMD5KeyChainEntry=rlMD5KeyChainEntry, PYSNMP_MODULE_ID=rlDigitalKeyManage, rlMD5KeyChainKeyStopAccept=rlMD5KeyChainKeyStopAccept, rlMD5KeyChainKeyValidForAccept=rlMD5KeyChainKeyValidForAccept, rlMD5KeyChainKeyValidForGenerate=rlMD5KeyChainKeyValidForGenerate, rlMD5KeyChainTable=rlMD5KeyChainTable)
