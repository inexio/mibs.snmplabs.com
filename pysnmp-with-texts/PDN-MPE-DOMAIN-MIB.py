#
# PySNMP MIB module PDN-MPE-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-DOMAIN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mpe_domain, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-domain")
VnidTaggingState, VnidRange, SwitchState, ClientState = mibBuilder.importSymbols("PDN-TC", "VnidTaggingState", "VnidRange", "SwitchState", "ClientState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter32, Bits, Gauge32, ModuleIdentity, Unsigned32, NotificationType, Counter64, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter32", "Bits", "Gauge32", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter64", "iso", "Integer32")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
mpePdnDomainMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1))
mpePdnDomainMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 2))
mpePdnCardGeneralParams = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1))
mpePdnCardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2))
mpePdnCardGeneralParamsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnCardGeneralParamsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardGeneralParamsTable.setDescription('A table that allows configuration of a Card VNID state.')
mpePdnCardGeneralParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnCardGeneralParamsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardGeneralParamsEntry.setDescription('A list of information for Card VNID.')
mpePdnCardGeneralParamsVNIDMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1, 1), VnidTaggingState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardGeneralParamsVNIDMode.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardGeneralParamsVNIDMode.setDescription('The state of VNID tagging on the card.')
mpePdnCardGeneralParamsAdditionalClientsAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnCardGeneralParamsAdditionalClientsAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardGeneralParamsAdditionalClientsAvailable.setDescription('This object contains the current number of unallocated client entries in the client table')
mpePdnCardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1), )
if mibBuilder.loadTexts: mpePdnCardConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigTable.setDescription('A table that contains information about Mux Forwarding, IP Filtering, IP Scoping and domain name for each VNID.')
mpePdnCardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "PDN-MPE-DOMAIN-MIB", "mpePdnCardConfigVnidId"))
if mibBuilder.loadTexts: mpePdnCardConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigEntry.setDescription('A list of configuration information for each VNID.')
mpePdnCardConfigVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 1), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpePdnCardConfigVnidId.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigVnidId.setDescription('The VNID Id number of the virtual network for which this entry contains management information.')
mpePdnCardConfigDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigDomainName.setDescription('The Domain name of the ISP for this VNID. The default value for this object is a blank string')
mpePdnCardConfigMuxFwd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 3), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigMuxFwd.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigMuxFwd.setDescription('This object shows if Mux Forwarding has been enabled or disabled by the user.')
mpePdnCardConfigIPFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 4), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigIPFiltering.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigIPFiltering.setDescription('This object shows if IP Filtering has been enabled or disabled by the user.')
mpePdnCardConfigIPScoping = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 5), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigIPScoping.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigIPScoping.setDescription('This object shows if IP Scoping has been enabled or disabled by the user.')
mpePdnCardConfigVnidAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 6), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigVnidAuth.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigVnidAuth.setDescription('This object shows if VNID authorization has been enabled or disabled by the user. When this obect is is enable, only interfaces bound to this VNID will accept packets with this VNID.')
mpePdnCardConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnCardConfigRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnCardConfigRowStatus.setDescription('This object is used to create a new row or or delete an existing row in this table')
mibBuilder.exportSymbols("PDN-MPE-DOMAIN-MIB", mpePdnCardConfigEntry=mpePdnCardConfigEntry, mpePdnCardConfigDomainName=mpePdnCardConfigDomainName, mpePdnDomainMIBTraps=mpePdnDomainMIBTraps, mpePdnDomainMIBObjects=mpePdnDomainMIBObjects, mpePdnCardGeneralParamsAdditionalClientsAvailable=mpePdnCardGeneralParamsAdditionalClientsAvailable, mpePdnCardGeneralParamsVNIDMode=mpePdnCardGeneralParamsVNIDMode, mpePdnCardConfigVnidId=mpePdnCardConfigVnidId, mpePdnCardConfigIPScoping=mpePdnCardConfigIPScoping, mpePdnCardConfigRowStatus=mpePdnCardConfigRowStatus, mpePdnCardGeneralParamsTable=mpePdnCardGeneralParamsTable, mpePdnCardConfigIPFiltering=mpePdnCardConfigIPFiltering, mpePdnCardConfigVnidAuth=mpePdnCardConfigVnidAuth, mpePdnCardGeneralParamsEntry=mpePdnCardGeneralParamsEntry, mpePdnCardConfigTable=mpePdnCardConfigTable, mpePdnCardConfigMuxFwd=mpePdnCardConfigMuxFwd, mpePdnCardConfig=mpePdnCardConfig, mpePdnCardGeneralParams=mpePdnCardGeneralParams)
