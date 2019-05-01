#
# PySNMP MIB module CISCO-CDSTV-INGEST-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, TimeTicks, Gauge32, IpAddress, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Integer32, Unsigned32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Gauge32", "IpAddress", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCdstvIngestTuningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 750))
ciscoCdstvIngestTuningMIB.setRevisions(('2010-06-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-cds@cisco.com')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setDescription("This MIB module defines ingest tuning configuration objects that facilitate the management of the Cisco Content Delivery System for TV (CDS-TV) product family. CDS-TV is a suite of products and software applications providing ingest, storage, caching, streaming, playout and on-demand delivery of video to television or set-top-box clients. Abbreviations: CCP Cache Control Protocol CDS Content Delivery System CORBA Common Object Request Broker Architecture ISA Interactive Services Architecture ISV Integrated Streamer-Vault FSI File Service Interface FTP File Transfer Protocol MPEG Motion Picture Experts Group MSA Managed Services Architecture RTSP Real-Time Streaming Protocol SOAP Simple Object Access Protocol STB Set-Top Box VOD Video On-Demand Common terms: Catcher: Device responsible for receiving content (typically via satellite dishes and antennae) from content providers or from a Headend-In-The-Sky. Content Ingest: Acquisition of content from a source such as a catcher or an FTP server for storing it locally and making it available to streamers as needed. Device Roles: Vault: Content delivery application responsible for ingesting and storing video content and making it available to streamers and/or caching nodes. Caching Nodes: Content delivery application responsible for caching content from vault (using CCP) and then streaming content out to streamers over HTTP or CCP. Streamer: Content delivery application responsible for streaming video out to STB's. ISV: Content delivery application capable of acting as both a vault and as a streamer in a single device.")
ciscoCdstvIngestTuningMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 0))
ciscoCdstvIngestTuningMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1))
ciscoCdstvIngestTuningMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2))
ciscoCdstvIngestTuningMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1))
cdstvTrickModeSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1), )
if mibBuilder.loadTexts: cdstvTrickModeSpeedTable.setStatus('current')
if mibBuilder.loadTexts: cdstvTrickModeSpeedTable.setDescription('A table of the trick-mode speed settings for ingest.')
cdstvTrickModeSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeedIndex"))
if mibBuilder.loadTexts: cdstvTrickModeSpeedEntry.setStatus('current')
if mibBuilder.loadTexts: cdstvTrickModeSpeedEntry.setDescription('An entry (conceptual row) in the ingest trick-mode speed settings table. Rows are added for each configured trick-mode speed setting and deleted if a previously configured trick-mode is disabled. Note that trick modes need not be in ascending or descending order, and gaps are allowed, e.g. 2, -8, 16, -4 is a valid sequence of trick-mode entries.')
cdstvTrickModeSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdstvTrickModeSpeedIndex.setStatus('current')
if mibBuilder.loadTexts: cdstvTrickModeSpeedIndex.setDescription('An index into the table containing the ingest trick-mode speed settings.')
cdstvTrickModeSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-127, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvTrickModeSpeed.setStatus('current')
if mibBuilder.loadTexts: cdstvTrickModeSpeed.setDescription('This object specifies a trick-mode speed for ingested content.')
cdstvServerIngestMPEGSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2))
cdstvServerPIDStandardization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerPIDStandardization.setStatus('current')
if mibBuilder.loadTexts: cdstvServerPIDStandardization.setDescription('This object specifies whether the MPEG-2 video assets have their program identifiers (PIDs) standardized at ingest so that most assets use the same PIDs. enabled(1) - PIDs for video assets are standardized at ingest disabled(2) - PIDs for video assets are not standardized at ingest')
cdstvServerSequenceEndRemove = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSequenceEndRemove.setStatus('current')
if mibBuilder.loadTexts: cdstvServerSequenceEndRemove.setDescription('This object specifies whether a SEQ END header that is present at the end of the asset (and only at the end) is removed on ingest. enabled(1) - SEQ END header is removed on ingest disabled(2) - SEQ END header is not removed on ingest')
cdstvServerRateStandardize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerRateStandardize.setStatus('current')
if mibBuilder.loadTexts: cdstvServerRateStandardize.setDescription('This object specifies whether the MPEG-2 video assets have their rates standardized at ingest so that most assets use one of two standard rates, 3.75 Mbps for Standard Definition (SD) assets or 15 Mbps for High Definition (HD) assets. enabled(1) - Video asset rates are standardized at ingest disabled(2) - Video asset rates are not standardized at ingest')
ciscoCdstvIngestTuningMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2))
ciscoCdstvIngestTuningMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "ciscoCdstvIngestTuningMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBCompliance = ciscoCdstvIngestTuningMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIBCompliance.setDescription('The compliance statement for the entities which implement the Cisco CDS TV Ingest Tuning MIB.')
ciscoCdstvIngestTuningMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeed"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerPIDStandardization"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerSequenceEndRemove"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerRateStandardize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBMainObjectGroup = ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIBMainObjectGroup.setDescription('A collection of objects that provide status of ingest tuning configuration.')
mibBuilder.exportSymbols("CISCO-CDSTV-INGEST-TUNING-MIB", ciscoCdstvIngestTuningMIBCompliances=ciscoCdstvIngestTuningMIBCompliances, cdstvTrickModeSpeedEntry=cdstvTrickModeSpeedEntry, ciscoCdstvIngestTuningMIBCompliance=ciscoCdstvIngestTuningMIBCompliance, cdstvTrickModeSpeedIndex=cdstvTrickModeSpeedIndex, cdstvTrickModeSpeedTable=cdstvTrickModeSpeedTable, cdstvServerPIDStandardization=cdstvServerPIDStandardization, ciscoCdstvIngestTuningMIBMainObjectGroup=ciscoCdstvIngestTuningMIBMainObjectGroup, PYSNMP_MODULE_ID=ciscoCdstvIngestTuningMIB, cdstvTrickModeSpeed=cdstvTrickModeSpeed, cdstvServerRateStandardize=cdstvServerRateStandardize, ciscoCdstvIngestTuningMIBGroups=ciscoCdstvIngestTuningMIBGroups, ciscoCdstvIngestTuningMIB=ciscoCdstvIngestTuningMIB, cdstvServerIngestMPEGSettings=cdstvServerIngestMPEGSettings, ciscoCdstvIngestTuningMIBNotifs=ciscoCdstvIngestTuningMIBNotifs, ciscoCdstvIngestTuningMIBObjects=ciscoCdstvIngestTuningMIBObjects, cdstvServerSequenceEndRemove=cdstvServerSequenceEndRemove, ciscoCdstvIngestTuningMIBConform=ciscoCdstvIngestTuningMIBConform)
