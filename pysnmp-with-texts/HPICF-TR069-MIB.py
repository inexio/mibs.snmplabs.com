#
# PySNMP MIB module HPICF-TR069-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-TR069-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter64, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, IpAddress, Counter32, MibIdentifier, Integer32, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "IpAddress", "Counter32", "MibIdentifier", "Integer32", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
hpicfTR069MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98))
hpicfTR069MIB.setRevisions(('2014-03-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfTR069MIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hpicfTR069MIB.setLastUpdated('201403030000Z')
if mibBuilder.loadTexts: hpicfTR069MIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfTR069MIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfTR069MIB.setDescription('This MIB defines HP proprietary objects used to configure the TR-069 feature.')
hpicfTR069Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 0))
hpicfTR069Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1))
hpicfTR069Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2))
hpicfTR069EnableCWMP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069EnableCWMP.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069EnableCWMP.setDescription('Enable TR-069 on the device.')
hpicfTR069CWMPDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("device", 1), ("gateway", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CWMPDeviceType.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069CWMPDeviceType.setDescription('The working mode of the device. By default, the device operates in gateway mode. CWMP should be disabled before changing modes.')
hpicfTR069AcsUrl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsUrl.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsUrl.setDescription('The URL used by TR-069 to connect to the ACS. The value should be a valid HTTP or HTTPS URL.')
hpicfTR069AcsUrlOrigin = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("config", 2), ("dhcp", 3), ("acs", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069AcsUrlOrigin.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsUrlOrigin.setDescription('The source of the ACS URL. none - no ACS URL set config - from the device configuration file dhcp - from a DHCP server response acs - from the ACS itself')
hpicfTR069AcsProxyUrl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsProxyUrl.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsProxyUrl.setDescription('The URL used by TR-069 to connect to a proxy server in order to reach the ACS. The value should be a valid HTTP or HTTPS URL.')
hpicfTR069AcsUsername = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsUsername.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsUsername.setDescription('The username for HTTP authentication with the ACS.')
hpicfTR069AcsPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsPassword.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsPassword.setDescription('The plaintext password for HTTP authentication with the ACS. This object always returns an empty string when read.')
hpicfTR069AcsPasswordEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069AcsPasswordEncrypted.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsPasswordEncrypted.setDescription("An encrypted form of the ACS password. The value should be an encrypted password previously read from a compatible HP Networking device. This object can only be read or written when hpSwitchAuthenticationEncryptCredentialsMethod is set to a value other than 'none' and cannot be set at the same time as hpicfTR069AcsPassword.")
hpicfTR069AcsConnectRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069AcsConnectRetryInterval.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069AcsConnectRetryInterval.setDescription('The ACS connection retry interval.')
hpicfTR069CpeUsername = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpeUsername.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069CpeUsername.setDescription('The username for HTTP authentication with the TR-069 client.')
hpicfTR069CpePassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpePassword.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069CpePassword.setDescription('The plaintext password for HTTP authentication with the TR-069 client. This object always returns an empty string when read.')
hpicfTR069CpePasswordEncrypted = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTR069CpePasswordEncrypted.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069CpePasswordEncrypted.setDescription("An encrypted form of the client password. The value should be an encrypted password previously read from a compatible HP Networking device. This object can only be read or written when hpSwitchAuthenticationEncryptCredentialsMethod is set to a value other than 'none' and cannot be set at the same time as hpicfTR069CpePassword.")
hpicfTR069CpeWaitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 13), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069CpeWaitTimeout.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069CpeWaitTimeout.setDescription('The close-wait timeout of the ACS connection.')
hpicfTR069PeriodicInformEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformEnable.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069PeriodicInformEnable.setDescription('The periodic inform message setting specified by the ACS.')
hpicfTR069PeriodicInformInterval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformInterval.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069PeriodicInformInterval.setDescription('The periodic inform interval in seconds specified by the ACS.')
hpicfTR069PeriodicInformTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 1, 16), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfTR069PeriodicInformTime.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069PeriodicInformTime.setDescription('The date and time to send inform messages specified by the ACS.')
hpicfTR069MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1))
hpicfTR069MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2))
hpicfTR069MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 1, 1)).setObjects(("HPICF-TR069-MIB", "hpicfTR069Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTR069MIBCompliance = hpicfTR069MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069MIBCompliance.setDescription('The compliance statement for HP switches implementing the HPICF-TR069 MIB.')
hpicfTR069Group = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98, 2, 2, 1)).setObjects(("HPICF-TR069-MIB", "hpicfTR069EnableCWMP"), ("HPICF-TR069-MIB", "hpicfTR069CWMPDeviceType"), ("HPICF-TR069-MIB", "hpicfTR069AcsUrl"), ("HPICF-TR069-MIB", "hpicfTR069AcsUrlOrigin"), ("HPICF-TR069-MIB", "hpicfTR069AcsProxyUrl"), ("HPICF-TR069-MIB", "hpicfTR069AcsUsername"), ("HPICF-TR069-MIB", "hpicfTR069AcsPassword"), ("HPICF-TR069-MIB", "hpicfTR069AcsPasswordEncrypted"), ("HPICF-TR069-MIB", "hpicfTR069AcsConnectRetryInterval"), ("HPICF-TR069-MIB", "hpicfTR069CpeUsername"), ("HPICF-TR069-MIB", "hpicfTR069CpePassword"), ("HPICF-TR069-MIB", "hpicfTR069CpePasswordEncrypted"), ("HPICF-TR069-MIB", "hpicfTR069CpeWaitTimeout"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformEnable"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformInterval"), ("HPICF-TR069-MIB", "hpicfTR069PeriodicInformTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTR069Group = hpicfTR069Group.setStatus('current')
if mibBuilder.loadTexts: hpicfTR069Group.setDescription('A collection of objects to support the TR-069 feature.')
mibBuilder.exportSymbols("HPICF-TR069-MIB", hpicfTR069AcsPassword=hpicfTR069AcsPassword, hpicfTR069Notifications=hpicfTR069Notifications, hpicfTR069AcsProxyUrl=hpicfTR069AcsProxyUrl, hpicfTR069CpePassword=hpicfTR069CpePassword, PYSNMP_MODULE_ID=hpicfTR069MIB, hpicfTR069CpePasswordEncrypted=hpicfTR069CpePasswordEncrypted, hpicfTR069Objects=hpicfTR069Objects, hpicfTR069MIBCompliances=hpicfTR069MIBCompliances, hpicfTR069Conformance=hpicfTR069Conformance, hpicfTR069AcsPasswordEncrypted=hpicfTR069AcsPasswordEncrypted, hpicfTR069CpeUsername=hpicfTR069CpeUsername, hpicfTR069MIBGroups=hpicfTR069MIBGroups, hpicfTR069PeriodicInformEnable=hpicfTR069PeriodicInformEnable, hpicfTR069AcsUrlOrigin=hpicfTR069AcsUrlOrigin, hpicfTR069MIB=hpicfTR069MIB, hpicfTR069Group=hpicfTR069Group, hpicfTR069CpeWaitTimeout=hpicfTR069CpeWaitTimeout, hpicfTR069MIBCompliance=hpicfTR069MIBCompliance, hpicfTR069AcsUrl=hpicfTR069AcsUrl, hpicfTR069PeriodicInformInterval=hpicfTR069PeriodicInformInterval, hpicfTR069AcsUsername=hpicfTR069AcsUsername, hpicfTR069EnableCWMP=hpicfTR069EnableCWMP, hpicfTR069PeriodicInformTime=hpicfTR069PeriodicInformTime, hpicfTR069CWMPDeviceType=hpicfTR069CWMPDeviceType, hpicfTR069AcsConnectRetryInterval=hpicfTR069AcsConnectRetryInterval)
