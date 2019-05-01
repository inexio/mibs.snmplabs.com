#
# PySNMP MIB module CISCO-DMN-DSG-PRODUCTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-PRODUCTION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, TimeTicks, Counter64, IpAddress, Bits, ModuleIdentity, NotificationType, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "TimeTicks", "Counter64", "IpAddress", "Bits", "ModuleIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGProd = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21))
ciscoDSGProd.setRevisions(('2010-08-24 07:00', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGProd.setRevisionsDescriptions(('V01.00.01 2010-08-24 Added itmes : prodBoardModelNum, prodBoardModelName, prodBoardCatalogNum, prodBoardCustomerCode and prodBoardFpgaType.', 'V01.00.00 2009-12-20 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGProd.setLastUpdated('201008240700Z')
if mibBuilder.loadTexts: ciscoDSGProd.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGProd.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGProd.setDescription('Cisco Production MIB.')
prodInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1))
prodHostName = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prodHostName.setStatus('current')
if mibBuilder.loadTexts: prodHostName.setDescription('User Configurable hostname of this Unit.')
prodTrackingId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodTrackingId.setStatus('current')
if mibBuilder.loadTexts: prodTrackingId.setDescription('Unit Tracking ID.')
prodModelNo = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodModelNo.setStatus('current')
if mibBuilder.loadTexts: prodModelNo.setDescription('Model Number.')
prodModelName = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodModelName.setStatus('current')
if mibBuilder.loadTexts: prodModelName.setDescription('Model Name.')
prodCatalogNo = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodCatalogNo.setStatus('current')
if mibBuilder.loadTexts: prodCatalogNo.setDescription('Catalogue Number.')
prodCustomerCode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodCustomerCode.setStatus('current')
if mibBuilder.loadTexts: prodCustomerCode.setDescription('Customer Code.')
prodLimitVer = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodLimitVer.setStatus('current')
if mibBuilder.loadTexts: prodLimitVer.setDescription('Oldest Compatible Application Version.')
prodFPGADesignation = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prodFPGADesignation.setStatus('current')
if mibBuilder.loadTexts: prodFPGADesignation.setDescription('Production FPGA Designation.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-PRODUCTION-MIB", prodFPGADesignation=prodFPGADesignation, prodHostName=prodHostName, PYSNMP_MODULE_ID=ciscoDSGProd, prodInfo=prodInfo, prodTrackingId=prodTrackingId, prodLimitVer=prodLimitVer, prodModelName=prodModelName, prodCatalogNo=prodCatalogNo, prodCustomerCode=prodCustomerCode, prodModelNo=prodModelNo, ciscoDSGProd=ciscoDSGProd)
