#
# PySNMP MIB module SNMP-USM-DH-OBJECTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-USM-DH-OBJECTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, experimental, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Gauge32, Counter32, Bits, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "experimental", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Gauge32", "Counter32", "Bits", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmDHObjectsMIB = ModuleIdentity((1, 3, 6, 1, 3, 101))
snmpUsmDHObjectsMIB.setRevisions(('2000-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setRevisionsDescriptions(('Initial version published as RFC 2786.',))
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setLastUpdated('200003060000Z')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setOrganization('Excite@Home')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setContactInfo('Author: Mike StJohns Postal: Excite@Home 450 Broadway Redwood City, CA 94063 Email: stjohns@corp.home.net Phone: +1-650-556-5368')
if mibBuilder.loadTexts: snmpUsmDHObjectsMIB.setDescription("The management information definitions for providing forward secrecy for key changes for the usmUserTable, and for providing a method for 'kickstarting' access to the agent via a Diffie-Helman key agreement.")
usmDHKeyObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1))
usmDHKeyConformance = MibIdentifier((1, 3, 6, 1, 3, 101, 2))
class DHKeyChange(TextualConvention, OctetString):
    reference = '-- Diffie-Hellman Key-Agreement Standard, PKCS #3; RSA Laboratories, November 1993'
    description = "Upon initialization, or upon creation of a row containing an object of this type, and after any successful SET of this value, a GET of this value returns 'y' where y = g^xa MOD p, and where g is the base from usmDHParameters, p is the prime from usmDHParameters, and xa is a new random integer selected by the agent in the interval 2^(l-1) <= xa < 2^l < p-1. 'l' is the optional privateValueLength from usmDHParameters in bits. If 'l' is omitted, then xa (and xr below) is selected in the interval 0 <= xa < p-1. y is expressed as an OCTET STRING 'PV' of length 'k' which satisfies k y = SUM 2^(8(k-i)) PV'i i=1 where PV1,...,PVk are the octets of PV from first to last, and where PV1 <> 0. A successful SET consists of the value 'y' expressed as an OCTET STRING as above concatenated with the value 'z'(expressed as an OCTET STRING in the same manner as y) where z = g^xr MOD p, where g, p and l are as above, and where xr is a new random integer selected by the manager in the interval 2^(l-1) <= xr < 2^l < p-1. A SET to an object of this type will fail with the error wrongValue if the current 'y' does not match the 'y' portion of the value of the varbind for the object. (E.g. GET yout, SET concat(yin, z), yout <> yin). Note that the private values xa and xr are never transmitted from manager to device or vice versa, only the values y and z. Obviously, these values must be retained until a successful SET on the associated object. The shared secret 'sk' is calculated at the agent as sk = z^xa MOD p, and at the manager as sk = y^xr MOD p. Each object definition of this type MUST describe how to map from the shared secret 'sk' to the operational key value used by the protocols and operations related to the object. In general, if n bits of key are required, the author suggests using the n right-most bits of the shared secret as the operational key value."
    status = 'current'

usmDHPublicObjects = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 1))
usmDHParameters = MibScalar((1, 3, 6, 1, 3, 101, 1, 1, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmDHParameters.setReference('-- Diffie-Hellman Key-Agreement Standard, PKCS #3, RSA Laboratories, November 1993 -- The Internet Key Exchange, RFC 2409, November 1998, Sec 6.1, 6.2')
if mibBuilder.loadTexts: usmDHParameters.setStatus('current')
if mibBuilder.loadTexts: usmDHParameters.setDescription('The public Diffie-Hellman parameters for doing a Diffie-Hellman key agreement for this device. This is encoded as an ASN.1 DHParameter per PKCS #3, section 9. E.g. DHParameter ::= SEQUENCE { prime INTEGER, -- p base INTEGER, -- g privateValueLength INTEGER OPTIONAL } Implementors are encouraged to use either the values from Oakley Group 1 or the values of from Oakley Group 2 as specified in RFC-2409, The Internet Key Exchange, Section 6.1, 6.2 as the default for this object. Other values may be used, but the security properties of those values MUST be well understood and MUST meet the requirements of PKCS #3 for the selection of Diffie-Hellman primes. In addition, any time usmDHParameters changes, all values of type DHKeyChange will change and new random numbers MUST be generated by the agent for each DHKeyChange object.')
usmDHUserKeyTable = MibTable((1, 3, 6, 1, 3, 101, 1, 1, 2), )
if mibBuilder.loadTexts: usmDHUserKeyTable.setStatus('current')
if mibBuilder.loadTexts: usmDHUserKeyTable.setDescription("This table augments and extends the usmUserTable and provides 4 objects which exactly mirror the objects in that table with the textual convention of 'KeyChange'. This extension allows key changes to be done in a manner where the knowledge of the current secret plus knowledge of the key change data exchanges (e.g. via wiretapping) will not reveal the new key.")
usmDHUserKeyEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 1, 2, 1), )
usmUserEntry.registerAugmentions(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserKeyEntry"))
usmDHUserKeyEntry.setIndexNames(*usmUserEntry.getIndexNames())
if mibBuilder.loadTexts: usmDHUserKeyEntry.setStatus('current')
if mibBuilder.loadTexts: usmDHUserKeyEntry.setDescription('A row of DHKeyChange objects which augment or replace the functionality of the KeyChange objects in the base table row.')
usmDHUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 1), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserAuthKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserAuthKeyChange.setDescription("The object used to change any given user's Authentication Key using a Diffie-Hellman key exchange. The right-most n bits of the shared secret 'sk', where 'n' is the number of bits required for the protocol defined by usmUserAuthProtocol, are installed as the operational authentication key for this row after a successful SET.")
usmDHUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 2), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnAuthKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserOwnAuthKeyChange.setDescription("The object used to change the agents own Authentication Key using a Diffie-Hellman key exchange. The right-most n bits of the shared secret 'sk', where 'n' is the number of bits required for the protocol defined by usmUserAuthProtocol, are installed as the operational authentication key for this row after a successful SET.")
usmDHUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 3), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserPrivKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserPrivKeyChange.setDescription("The object used to change any given user's Privacy Key using a Diffie-Hellman key exchange. The right-most n bits of the shared secret 'sk', where 'n' is the number of bits required for the protocol defined by usmUserPrivProtocol, are installed as the operational privacy key for this row after a successful SET.")
usmDHUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 1, 2, 1, 4), DHKeyChange()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmDHUserOwnPrivKeyChange.setStatus('current')
if mibBuilder.loadTexts: usmDHUserOwnPrivKeyChange.setDescription("The object used to change the agent's own Privacy Key using a Diffie-Hellman key exchange. The right-most n bits of the shared secret 'sk', where 'n' is the number of bits required for the protocol defined by usmUserPrivProtocol, are installed as the operational privacy key for this row after a successful SET.")
usmDHKickstartGroup = MibIdentifier((1, 3, 6, 1, 3, 101, 1, 2))
usmDHKickstartTable = MibTable((1, 3, 6, 1, 3, 101, 1, 2, 1), )
if mibBuilder.loadTexts: usmDHKickstartTable.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartTable.setDescription("A table of mappings between zero or more Diffie-Helman key agreement values and entries in the usmUserTable. Entries in this table are created by providing the associated device with a Diffie-Helman public value and a usmUserName/usmUserSecurityName pair during initialization. How these values are provided is outside the scope of this MIB, but could be provided manually, or through a configuration file. Valid public value/name pairs result in the creation of a row in this table as well as the creation of an associated row (with keys derived as indicated) in the usmUserTable. The actual access the related usmSecurityName has is dependent on the entries in the VACM tables. In general, an implementor will specify one or more standard security names and will provide entries in the VACM tables granting various levels of access to those names. The actual content of the VACM table is beyond the scope of this MIB. Note: This table is expected to be readable without authentication using the usmUserSecurityName 'dhKickstart'. See the conformance statements for details.")
usmDHKickstartEntry = MibTableRow((1, 3, 6, 1, 3, 101, 1, 2, 1, 1), ).setIndexNames((0, "SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartIndex"))
if mibBuilder.loadTexts: usmDHKickstartEntry.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartEntry.setDescription("An entry in the usmDHKickstartTable. The agent SHOULD either delete this entry or mark it as inactive upon a successful SET of any of the KeyChange-typed objects in the usmUserEntry or upon a successful SET of any of the DHKeyChange-typed objects in the usmDhKeyChangeEntry where the related usmSecurityName (e.g. row of usmUserTable or row of ushDhKeyChangeTable) equals this entry's usmDhKickstartSecurityName. In otherwords, once you've changed one or more of the keys for a row in usmUserTable with a particular security name, the row in this table with that same security name is no longer useful or meaningful.")
usmDHKickstartIndex = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: usmDHKickstartIndex.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartIndex.setDescription('Index value for this row.')
usmDHKickstartMyPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setReference('-- Diffie-Hellman Key-Agreement Standard, PKCS#3v1.4; RSA Laboratories, November 1993 -- The Internet Key Exchange, RFC2409; Harkins, D., Carrel, D.; November 1998')
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartMyPublic.setDescription("The agent's Diffie-Hellman public value for this row. At initialization, the agent generates a random number and derives its public value from that number. This public value is published here. This public value 'y' equals g^r MOD p where g is the from the set of Diffie-Hellman parameters, p is the prime from those parameters, and r is a random integer selected by the agent in the interval 2^(l-1) <= r < p-1 < 2^l. If l is unspecified, then r is a random integer selected in the interval 0 <= r < p-1 The public value is expressed as an OCTET STRING 'PV' of length 'k' which satisfies k y = SUM 2^(8(k-i)) PV'i i = 1 where PV1,...,PVk are the octets of PV from first to last, and where PV1 != 0. The following DH parameters (Oakley group #2, RFC 2409, sec 6.1, 6.2) are used for this object: g = 2 p = FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1 29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245 E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE65381 FFFFFFFF FFFFFFFF l=1024 ")
usmDHKickstartMgrPublic = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setReference('-- Password-Based Cryptography Standard, PKCS#5v2.0; RSA Laboratories, March 1999 -- Applied Cryptography, 2nd Ed.; B. Schneier, Counterpane Systems; John Wiley & Sons, 1996')
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartMgrPublic.setDescription("The manager's Diffie-Hellman public value for this row. Note that this value is not set via the SNMP agent, but may be set via some out of band method, such as the device's configuration file. The manager calculates this value in the same manner and using the same parameter set as the agent does. E.g. it selects a random number 'r', calculates y = g^r mod p and provides 'y' as the public number expressed as an OCTET STRING. See usmDHKickstartMyPublic for details. When this object is set with a valid value during initialization, a row is created in the usmUserTable with the following values: usmUserEngineID localEngineID usmUserName [value of usmDHKickstartSecurityName] usmUserSecurityName [value of usmDHKickstartSecurityName] usmUserCloneFrom ZeroDotZero usmUserAuthProtocol usmHMACMD5AuthProtocol usmUserAuthKeyChange -- derived from set value usmUserOwnAuthKeyChange -- derived from set value usmUserPrivProtocol usmDESPrivProtocol usmUserPrivKeyChange -- derived from set value usmUserOwnPrivKeyChange -- derived from set value usmUserPublic '' usmUserStorageType permanent usmUserStatus active A shared secret 'sk' is calculated at the agent as sk = mgrPublic^r mod p where r is the agents random number and p is the DH prime from the common parameters. The underlying privacy key for this row is derived from sk by applying the key derivation function PBKDF2 defined in PKCS#5v2.0 with a salt of 0xd1310ba6, and iterationCount of 500, a keyLength of 16 (for usmDESPrivProtocol), and a prf (pseudo random function) of 'id-hmacWithSHA1'. The underlying authentication key for this row is derived from sk by applying the key derivation function PBKDF2 with a salt of 0x98dfb5ac , an interation count of 500, a keyLength of 16 (for usmHMAC5AuthProtocol), and a prf of 'id-hmacWithSHA1'. Note: The salts are the first two words in the ks0 [key schedule 0] of the BLOWFISH cipher from 'Applied Cryptography' by Bruce Schnier - they could be any relatively random string of bits. The manager can use its knowledge of its own random number and the agent's public value to kickstart its access to the agent in a secure manner. Note that the security of this approach is directly related to the strength of the authorization security of the out of band provisioning of the managers public value (e.g. the configuration file), but is not dependent at all on the strength of the confidentiality of the out of band provisioning data.")
usmDHKickstartSecurityName = MibTableColumn((1, 3, 6, 1, 3, 101, 1, 2, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmDHKickstartSecurityName.setStatus('current')
if mibBuilder.loadTexts: usmDHKickstartSecurityName.setDescription("The usmUserName and usmUserSecurityName in the usmUserTable associated with this row. This is provided in the same manner and at the same time as the usmDHKickstartMgrPublic value - e.g. possibly manually, or via the device's configuration file.")
usmDHKeyMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 1))
usmDHKeyMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 101, 2, 2))
usmDHKeyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 101, 2, 1, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyMIBBasicGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyParamGroup"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKeyKickstartGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBCompliance = usmDHKeyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyMIBCompliance.setDescription('The compliance statement for this module.')
usmDHKeyMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 1)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnAuthKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserPrivKeyChange"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHUserOwnPrivKeyChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyMIBBasicGroup = usmDHKeyMIBBasicGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyMIBBasicGroup.setDescription('')
usmDHKeyParamGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 2)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHParameters"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyParamGroup = usmDHKeyParamGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyParamGroup.setDescription('The mandatory object for all MIBs which use the DHKeyChange textual convention.')
usmDHKeyKickstartGroup = ObjectGroup((1, 3, 6, 1, 3, 101, 2, 2, 3)).setObjects(("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMyPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartMgrPublic"), ("SNMP-USM-DH-OBJECTS-MIB", "usmDHKickstartSecurityName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmDHKeyKickstartGroup = usmDHKeyKickstartGroup.setStatus('current')
if mibBuilder.loadTexts: usmDHKeyKickstartGroup.setDescription('The objects used for kickstarting one or more SNMPv3 USM associations via a configuration file or other out of band, non-confidential access.')
mibBuilder.exportSymbols("SNMP-USM-DH-OBJECTS-MIB", usmDHParameters=usmDHParameters, PYSNMP_MODULE_ID=snmpUsmDHObjectsMIB, usmDHUserPrivKeyChange=usmDHUserPrivKeyChange, usmDHKeyConformance=usmDHKeyConformance, usmDHKickstartSecurityName=usmDHKickstartSecurityName, DHKeyChange=DHKeyChange, usmDHKeyParamGroup=usmDHKeyParamGroup, usmDHUserOwnPrivKeyChange=usmDHUserOwnPrivKeyChange, usmDHKeyMIBBasicGroup=usmDHKeyMIBBasicGroup, usmDHUserOwnAuthKeyChange=usmDHUserOwnAuthKeyChange, usmDHKickstartIndex=usmDHKickstartIndex, usmDHUserKeyTable=usmDHUserKeyTable, usmDHKickstartEntry=usmDHKickstartEntry, usmDHUserAuthKeyChange=usmDHUserAuthKeyChange, usmDHPublicObjects=usmDHPublicObjects, usmDHUserKeyEntry=usmDHUserKeyEntry, usmDHKickstartTable=usmDHKickstartTable, usmDHKickstartMyPublic=usmDHKickstartMyPublic, usmDHKeyObjects=usmDHKeyObjects, usmDHKeyMIBCompliance=usmDHKeyMIBCompliance, usmDHKeyKickstartGroup=usmDHKeyKickstartGroup, usmDHKickstartMgrPublic=usmDHKickstartMgrPublic, snmpUsmDHObjectsMIB=snmpUsmDHObjectsMIB, usmDHKickstartGroup=usmDHKickstartGroup, usmDHKeyMIBGroups=usmDHKeyMIBGroups, usmDHKeyMIBCompliances=usmDHKeyMIBCompliances)
