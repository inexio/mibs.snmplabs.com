#
# PySNMP MIB module ENTERASYS-SSH-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-SSH-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, iso, ModuleIdentity, ObjectIdentity, Counter64, Unsigned32, NotificationType, Gauge32, IpAddress, TimeTicks, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "Counter64", "Unsigned32", "NotificationType", "Gauge32", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
etsysSshServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26))
etsysSshServerMIB.setRevisions(('2003-02-19 19:03', '2002-11-14 15:41', '2002-09-27 17:48', '2002-09-18 20:41',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysSshServerMIB.setRevisionsDescriptions(('The status of all of the objects in this MIB module were changed to deprecated.', 'Added dsa512 and rsa512 enumerations to the etsysSshOperKeyType and etsysSshAdminKeyType objects.', 'Added a completedPending enumeration to the etsysSshGenerateHostKeys object, and a none enumeration to the etsysSshOperKeyType object.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysSshServerMIB.setLastUpdated('200302191903Z')
if mibBuilder.loadTexts: etsysSshServerMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysSshServerMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 USA Phone: +1 603 332 9400 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysSshServerMIB.setDescription("This MIB module defines a portion of the SNMP enterprise MIBs under Enterasys Networks' enterprise OID pertaining to Secure Shell (SSH) system management functionality, specifically for embedded systems. This is a subset of the objects that would be required for a full-featured, host- based implementation. It provides configuration controls for Enterasys Networks' Secure Shell system management -- a feature that enhances system security by authenticating and encrypting the remote system management function.")
etsysSshObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1))
etsysSshGeneralBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1))
etsysSshNetworkBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 2))
etsysSshCryptoBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3))
etsysSshLoginBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4))
etsysSshServerKeyBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5))
etsysSshAuthBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6))
etsysSshEnabled = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshEnabled.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshEnabled.setDescription('Controls the operation of the Secure Shell server task on the embedded system. When enabled, the SSH server will accept connection requests and create a secure transport layer on which to transmit system configuration data.')
etsysSshEventLogFilter = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("information", 2), ("warning", 3), ("error", 4))).clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshEventLogFilter.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshEventLogFilter.setDescription('Specifies the filter for event log messages. Valid values are information, warning, and error. The values are defined as follows: none (1) Pass no messages. This is effectively a disable condition for Event Logging. information (2) Pass Informational Level, Warning Level and Error Level messages. warning (3) Pass Warning Level and Error Level messages. error (4) Pass Error Level messages only.')
etsysSshMaxConnections = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSshMaxConnections.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshMaxConnections.setDescription('Specifies the maximum number of simultaneous connections that the target system supports. This is an implementation restriction.')
etsysSshNumConnections = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshNumConnections.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshNumConnections.setDescription('Specifies the maximum number of simultaneous connections that the server will currently allow. This value must be less than or equal to etsysSshMaxConnections.')
etsysSshCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("anyStdCipher", 1), ("anyCipher", 2), ("des", 3), ("tripleDes", 4), ("blowfish", 5), ("arcFour", 6), ("twofish", 7), ("cast128", 8), ("aes", 9))).clone('anyStdCipher')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshCiphers.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshCiphers.setDescription("Specifies the ciphers to use for encrypting the session. Current enumerated types, DES, 3DES, Blowfish, Arcfour, Twofish, and CAST128 are supported. Special values to this option are any, anystd, that allows only standard (see below) ciphers, and anycipher that allows either any available cipher or excludes non-encrypting cipher mode none but allows all others. anystdcipher is the same as above, but includes only those ciphers mentioned in the IETF-SecSH-draft (excluding 'none').")
etsysSshMACs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("anyStdMac", 1), ("anyMac", 2), ("hmacSha1", 3), ("hmacSha1Dash96", 4), ("hmacMd5", 5), ("hmacMd5Dash96", 6), ("hmacRipemd160", 7), ("hmacRipemd160Dash96", 8))).clone('anyStdMac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshMACs.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshMACs.setDescription('Specifies the MAC (Message Authentication Code) algorithm to use for data integrity verification. Currently enumerated types, hmacSha1, hmacSha1Dash96, hmacMd5, hmacMd5Dash96, hmacRipemd160, and hmacRipemd160Dash96 are supported, of which hmacSha1, hmacSha1Dash96, hmacMd5, and hmacMd5Dash96 are included in all distributions. Special values to this option are anyStdMac, that allows only standard (see below) MACs, and anyMac that allows either any available MAC or excludes none but allows all others. AnyStdMac is the same as above, but includes only those MACs mentioned in the IETF-SecSH-draft (excluding none). ')
etsysSshRekeyIntervalSeconds = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshRekeyIntervalSeconds.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshRekeyIntervalSeconds.setDescription('Specifies the number of seconds after which the key exchange is done again. A value of 0 (zero) turns re-key requests off. This does not prevent the client from requesting re-keys. Note that not all clients support this function.')
etsysSshRandomSeed = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshRandomSeed.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshRandomSeed.setDescription('Specifies optional additional entropy information that will be merged with the seed for the random number generator.')
etsysSshLoginGraceTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshLoginGraceTime.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshLoginGraceTime.setDescription('The server disconnects after this many seconds if the user has not successfully been authenticated and logged in. The range limit is from 1 second to 1 hour.')
etsysSshIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(10)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshIdleTimeout.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshIdleTimeout.setDescription('Specifies the maximum number of minutes before a user is disconnected due to lack of activity. A value of zero means that there is no idle timeout.')
etsysSshBannerMessage = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 4, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshBannerMessage.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshBannerMessage.setDescription('Banner message that is displayed at the client before the login.')
etsysSshGenerateHostKeys = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notInitiated", 1), ("completed", 2), ("failed", 3), ("generate", 4), ("completedPending", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshGenerateHostKeys.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshGenerateHostKeys.setDescription('Causes the host to generate a new private/public host key pair, using the cipher algorithm currently selected in etsysSshAdminKeyType. Note that this can be compute intensive on many platforms. The meaning of the values are as follows: notInitiated (1) On a write, this is a no-operation, on a read, it indicates that no key material generation operation has ever been initiated, at least since the last reset to factory defaults initialization of the managed entity. No key material exists. completed (2) On a write, this is a no-operation, on a read, this indicates that a key pair has been successfully generated. failed (3) On a write, this is a no-operation, on a read, it indicates that the key generation operation has failed. generate (4) On a write, this causes the managed entity to generate a new key pair, on a read, it indicates that the managed entity is still working on creating the new keys. completedPending (5) On a write, this is a no-operation, on a read, this indicates that a key pair has been successfully generated but its use is pending due to another required operation, such as a reboot.')
etsysSshPublicHostKey = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSshPublicHostKey.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshPublicHostKey.setDescription("The host's public key, of type etsysSshOperKeyType.")
etsysSshAdminKeyType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("dsa768", 1), ("rsa768", 2), ("dsa1024", 3), ("rsa1024", 4), ("dsa2048", 5), ("rsa2048", 6), ("dsa3072", 7), ("rsa3072", 8), ("dsa512", 9), ("rsa512", 10))).clone('rsa1024')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshAdminKeyType.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshAdminKeyType.setDescription('Determines the type of the key pair to be (re)created on the next key (re)creation operation. The etsysSshOperKeyType object returns the type of key that is currently being used by the SSH server.')
etsysSshOperKeyType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99))).clone(namedValues=NamedValues(("dsa768", 1), ("rsa768", 2), ("dsa1024", 3), ("rsa1024", 4), ("dsa2048", 5), ("rsa2048", 6), ("dsa3072", 7), ("rsa3072", 8), ("dsa512", 9), ("rsa512", 10), ("none", 99))).clone('rsa1024')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSshOperKeyType.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshOperKeyType.setDescription('Indicates the type of the key pair currently in effect on the managed entity. The value of the etsysSshAdminKeyType object is copied to the etsysSshOperKeyType object upon successful completion of the (re)creation of a key pair. A value of none indicates that due to the failure of the initial key pair generation there is no active key pair.')
etsysSshPasswordGuesses = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshPasswordGuesses.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshPasswordGuesses.setDescription('Specifies the number of tries that the user has when attempting to authenticate using password authentication.')
etsysSshAllowedAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("allAuth", 1), ("password", 2), ("publickey", 3))).clone('password')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshAllowedAuthentications.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshAllowedAuthentications.setDescription('This specifies the authentications methods that are allowed. This is an enumerated list currently consisting of the following types: password, publickey. Each specifies an authentication method. With RequiredAuthentications, the administrator can force users to complete several authentications before they are considered authenticated.')
etsysSshRequiredAuthentications = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 1, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuth", 1), ("password", 2), ("publickey", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSshRequiredAuthentications.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshRequiredAuthentications.setDescription('Related to AllowedAuthentications, this is used to specify what authentication methods the users must complete before continuing. If this value is left zero, it does not mean that no authentications are required. It means that the client can authenticate itself with any of the authentications given in AllowedAuthentications. This parameter has no default. Note: This parameter has to be a subset for AllowedAuthentications. Otherwise, the server denies connection every time.')
etsysSshConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2))
etsysSshGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1))
etsysSshCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 2))
etsysSshBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 1)).setObjects(("ENTERASYS-SSH-SERVER-MIB", "etsysSshEnabled"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshMaxConnections"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshNumConnections"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshCiphers"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshMACs"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRekeyIntervalSeconds"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRandomSeed"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshGenerateHostKeys"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshPublicHostKey"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshAdminKeyType"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshOperKeyType"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshAllowedAuthentications"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshRequiredAuthentications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSshBaseGroup = etsysSshBaseGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshBaseGroup.setDescription('A collection of objects providing basic SSH server configuration on a managed entity.')
etsysSshAdvancedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 2)).setObjects(("ENTERASYS-SSH-SERVER-MIB", "etsysSshBannerMessage"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshLoginGraceTime"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshIdleTimeout"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshPasswordGuesses"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSshAdvancedGroup = etsysSshAdvancedGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshAdvancedGroup.setDescription('A collection of objects providing advanced feature support for configuration of the SSH server on the managed entity.')
etsysSshEventLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 1, 3)).setObjects(("ENTERASYS-SSH-SERVER-MIB", "etsysSshEventLogFilter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSshEventLogGroup = etsysSshEventLogGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshEventLogGroup.setDescription('A collection of objects to manage SSH event logs on the managed entity. Conditionally mandatory for all managed entities that implement the event log feature.')
etsysSshCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 26, 2, 2, 1)).setObjects(("ENTERASYS-SSH-SERVER-MIB", "etsysSshBaseGroup"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshAdvancedGroup"), ("ENTERASYS-SSH-SERVER-MIB", "etsysSshEventLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSshCompliance = etsysSshCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: etsysSshCompliance.setDescription('The compliance statement for devices that support the Enterasys Secure Shell (SSH) MIB.')
mibBuilder.exportSymbols("ENTERASYS-SSH-SERVER-MIB", etsysSshNumConnections=etsysSshNumConnections, etsysSshGeneralBranch=etsysSshGeneralBranch, etsysSshCompliance=etsysSshCompliance, etsysSshCompliances=etsysSshCompliances, etsysSshMACs=etsysSshMACs, etsysSshPublicHostKey=etsysSshPublicHostKey, etsysSshEnabled=etsysSshEnabled, etsysSshEventLogGroup=etsysSshEventLogGroup, PYSNMP_MODULE_ID=etsysSshServerMIB, etsysSshNetworkBranch=etsysSshNetworkBranch, etsysSshLoginGraceTime=etsysSshLoginGraceTime, etsysSshGenerateHostKeys=etsysSshGenerateHostKeys, etsysSshAdvancedGroup=etsysSshAdvancedGroup, etsysSshRequiredAuthentications=etsysSshRequiredAuthentications, etsysSshBaseGroup=etsysSshBaseGroup, etsysSshLoginBranch=etsysSshLoginBranch, etsysSshOperKeyType=etsysSshOperKeyType, etsysSshRekeyIntervalSeconds=etsysSshRekeyIntervalSeconds, etsysSshEventLogFilter=etsysSshEventLogFilter, etsysSshConformance=etsysSshConformance, etsysSshGroups=etsysSshGroups, etsysSshMaxConnections=etsysSshMaxConnections, etsysSshIdleTimeout=etsysSshIdleTimeout, etsysSshAuthBranch=etsysSshAuthBranch, etsysSshBannerMessage=etsysSshBannerMessage, etsysSshAdminKeyType=etsysSshAdminKeyType, etsysSshCiphers=etsysSshCiphers, etsysSshCryptoBranch=etsysSshCryptoBranch, etsysSshServerKeyBranch=etsysSshServerKeyBranch, etsysSshServerMIB=etsysSshServerMIB, etsysSshObjects=etsysSshObjects, etsysSshRandomSeed=etsysSshRandomSeed, etsysSshAllowedAuthentications=etsysSshAllowedAuthentications, etsysSshPasswordGuesses=etsysSshPasswordGuesses)
