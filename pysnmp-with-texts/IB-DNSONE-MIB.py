#
# PySNMP MIB module IB-DNSONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-DNSONE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ibDNSOne, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "ibDNSOne", "IbString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibIdentifier, Integer32, Unsigned32, enterprises, Gauge32, Counter32, Counter64, TimeTicks, NotificationType, ModuleIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "Integer32", "Unsigned32", "enterprises", "Gauge32", "Counter32", "Counter64", "TimeTicks", "NotificationType", "ModuleIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDnsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1))
ibDnsModule.setRevisions(('2010-03-23 00:00', '2005-06-09 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDnsModule.setRevisionsDescriptions(('Fixed smilint errors', 'DNS views', 'Added copyright', 'Creation of the MIB file',))
if mibBuilder.loadTexts: ibDnsModule.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: ibDnsModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDnsModule.setContactInfo('Please See IB-SMI-MIB.')
if mibBuilder.loadTexts: ibDnsModule.setDescription('This file defines the Infoblox DNS One MIB.')
ibZoneStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1), )
if mibBuilder.loadTexts: ibZoneStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: ibZoneStatisticsTable.setDescription('A table of named ZONE statistics.')
ibZoneStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1), ).setIndexNames((0, "IB-DNSONE-MIB", "ibBindZoneName"))
if mibBuilder.loadTexts: ibZoneStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: ibZoneStatisticsEntry.setDescription('A conceptual row of the ibZoneStatisticsEntry containing info about a particular zone in the default view.')
ibBindZoneName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneName.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneName.setDescription("DNS Zone name. The first one is global summary statistics. Index name for global statistics is 'summary'. All zones live in the default view.")
ibBindZoneSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneSuccess.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneSuccess.setDescription('Number of Successful responses since DNS process started.')
ibBindZoneReferral = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneReferral.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneReferral.setDescription('Number of DNS referrals since DNS process started.')
ibBindZoneNxRRset = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneNxRRset.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneNxRRset.setDescription('Number of DNS query received for non-existent record.')
ibBindZoneNxDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneNxDomain.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneNxDomain.setDescription('Number of DNS query received for non-existent domain.')
ibBindZoneRecursion = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneRecursion.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneRecursion.setDescription('Number of Queries received using recursion since DNS process started.')
ibBindZoneFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneFailure.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneFailure.setDescription('Number of Failed queries since DNS process started.')
ibZonePlusViewStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2), )
if mibBuilder.loadTexts: ibZonePlusViewStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: ibZonePlusViewStatisticsTable.setDescription('A table of named ZONE+VIEW statistics.')
ibZonePlusViewStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1), ).setIndexNames((0, "IB-DNSONE-MIB", "ibBindViewName"), (0, "IB-DNSONE-MIB", "ibBindZonePlusViewName"))
if mibBuilder.loadTexts: ibZonePlusViewStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: ibZonePlusViewStatisticsEntry.setDescription('A conceptual row of the ibZonePlusViewStatisticsEntry containing info about a particular zone in a particular view.')
ibBindZonePlusViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewName.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewName.setDescription("DNS Zone name. The first one in the default view is the global summary statistics. Index name for global statistics is 'summary'.")
ibBindZonePlusViewSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewSuccess.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewSuccess.setDescription('Number of Successful responses since DNS process started.')
ibBindZonePlusViewReferral = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewReferral.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewReferral.setDescription('Number of DNS referrals since DNS process started.')
ibBindZonePlusViewNxRRset = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewNxRRset.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewNxRRset.setDescription('Number of DNS query received for non-existent record.')
ibBindZonePlusViewNxDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewNxDomain.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewNxDomain.setDescription('Number of DNS query received for non-existent domain.')
ibBindZonePlusViewRecursion = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewRecursion.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewRecursion.setDescription('Number of Queries received using recursion since DNS process started.')
ibBindZonePlusViewFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZonePlusViewFailure.setStatus('current')
if mibBuilder.loadTexts: ibBindZonePlusViewFailure.setDescription('Number of Failed queries since DNS process started.')
ibBindViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 2, 1, 8), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindViewName.setStatus('current')
if mibBuilder.loadTexts: ibBindViewName.setDescription('DNS view name. Empty for default view and summary.')
ibDDNSUpdateStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3))
ibDDNSUpdateSuccess = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateSuccess.setStatus('current')
if mibBuilder.loadTexts: ibDDNSUpdateSuccess.setDescription('Number of successful dynamic DNS update.')
ibDDNSUpdateFailure = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateFailure.setStatus('current')
if mibBuilder.loadTexts: ibDDNSUpdateFailure.setDescription('Number of failure dynamic DNS update.')
ibDDNSUpdateReject = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdateReject.setStatus('current')
if mibBuilder.loadTexts: ibDDNSUpdateReject.setDescription('Number of dynamic DNS update rejects maybe due to permission failure.')
ibDDNSUpdatePrerequisiteReject = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 3, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDDNSUpdatePrerequisiteReject.setStatus('current')
if mibBuilder.loadTexts: ibDDNSUpdatePrerequisiteReject.setDescription('Number of dynamic DNS update rejects due to prerequisite failure.')
ibBindZoneTransferCount = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibBindZoneTransferCount.setStatus('current')
if mibBuilder.loadTexts: ibBindZoneTransferCount.setDescription('Number of zone transfer.')
mibBuilder.exportSymbols("IB-DNSONE-MIB", ibDnsModule=ibDnsModule, ibBindZonePlusViewRecursion=ibBindZonePlusViewRecursion, ibBindZoneNxDomain=ibBindZoneNxDomain, ibBindViewName=ibBindViewName, ibBindZonePlusViewNxRRset=ibBindZonePlusViewNxRRset, ibZoneStatisticsEntry=ibZoneStatisticsEntry, ibDDNSUpdateStatistics=ibDDNSUpdateStatistics, PYSNMP_MODULE_ID=ibDnsModule, ibBindZoneRecursion=ibBindZoneRecursion, ibZonePlusViewStatisticsEntry=ibZonePlusViewStatisticsEntry, ibBindZonePlusViewReferral=ibBindZonePlusViewReferral, ibZonePlusViewStatisticsTable=ibZonePlusViewStatisticsTable, ibBindZoneNxRRset=ibBindZoneNxRRset, ibDDNSUpdatePrerequisiteReject=ibDDNSUpdatePrerequisiteReject, ibDDNSUpdateSuccess=ibDDNSUpdateSuccess, ibBindZoneTransferCount=ibBindZoneTransferCount, ibBindZoneReferral=ibBindZoneReferral, ibBindZoneSuccess=ibBindZoneSuccess, ibBindZoneFailure=ibBindZoneFailure, ibBindZonePlusViewName=ibBindZonePlusViewName, ibBindZonePlusViewFailure=ibBindZonePlusViewFailure, ibDDNSUpdateFailure=ibDDNSUpdateFailure, ibBindZonePlusViewSuccess=ibBindZonePlusViewSuccess, ibBindZonePlusViewNxDomain=ibBindZonePlusViewNxDomain, ibDDNSUpdateReject=ibDDNSUpdateReject, ibZoneStatisticsTable=ibZoneStatisticsTable, ibBindZoneName=ibBindZoneName)
