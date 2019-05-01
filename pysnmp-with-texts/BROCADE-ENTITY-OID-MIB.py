#
# PySNMP MIB module BROCADE-ENTITY-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-ENTITY-OID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:40:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
products, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, MibIdentifier, ObjectIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, Integer32, Gauge32, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "ObjectIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "Integer32", "Gauge32", "TimeTicks", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
brcdEntityOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 17))
brcdEntityOIDMIB.setRevisions(('2013-02-06 09:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: brcdEntityOIDMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: brcdEntityOIDMIB.setLastUpdated('201302060930Z')
if mibBuilder.loadTexts: brcdEntityOIDMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: brcdEntityOIDMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: brcdEntityOIDMIB.setDescription("This module defines the object identifiers (OIDs) for various physical components on Brocade products. These OIDs are used for representing entPhysicalVendorType in Entity MIB's entPhysicalTable (RFC 4133). Copyright 1996-2012 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
brcdEntityOIDMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1))
brcdEntityOIDOther = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 1))
brcdEntityOIDUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 2))
brcdEntityOIDChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3))
brcdEntityOIDChassisUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 1))
brcdEntityOIDChassisNetIronCes2000Family = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2))
brcdEntityOIDChassisNetIronCes2024F = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 1))
brcdEntityOIDChassisNetIronCes2024C = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 2))
brcdEntityOIDChassisNetIronCes2048F = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 3))
brcdEntityOIDChassisNetIronCes2048C = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 4))
brcdEntityOIDChassisNetIronCes2048FX = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 5))
brcdEntityOIDChassisNetIronCes2048CX = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 6))
brcdEntityOIDChassisNetIronCes2024F4X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 7))
brcdEntityOIDChassisNetIronCes2024C4X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 2, 8))
brcdEntityOIDChassisNetIronCer2000Family = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3))
brcdEntityOIDChassisNetIronCer2024F = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 1))
brcdEntityOIDChassisNetIronCer2024C = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 2))
brcdEntityOIDChassisNetIronCer2048F = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 3))
brcdEntityOIDChassisNetIronCer2048C = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 4))
brcdEntityOIDChassisNetIronCer2048FX = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 5))
brcdEntityOIDChassisNetIronCer2048CX = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 6))
brcdEntityOIDChassisNetIronCer2024F4X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 7))
brcdEntityOIDChassisNetIronCer2024C4X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 3, 8))
brcdEntityOIDChassisNetIronXMRFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4))
brcdEntityOIDChassisNetIronXMR4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 1))
brcdEntityOIDChassisNetIronXMR8000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 2))
brcdEntityOIDChassisNetIronXMR16000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 3))
brcdEntityOIDChassisNetIronXMR32000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 4, 4))
brcdEntityOIDChassisMLXFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5))
brcdEntityOIDChassisMLX4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 1))
brcdEntityOIDChassisMLX8 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 2))
brcdEntityOIDChassisMLX16 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 3))
brcdEntityOIDChassisMLX32 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 5, 4))
brcdEntityOIDChassisMLXeFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6))
brcdEntityOIDChassisMLXe4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 1))
brcdEntityOIDChassisMLXe8 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 2))
brcdEntityOIDChassisMLXe16 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 3))
brcdEntityOIDChassisMLXe32 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 3, 6, 4))
brcdEntityOIDBackplane = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4))
brcdEntityOIDBackplaneUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 1))
brcdEntityOIDBackplaneNetIronFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2))
brcdEntityOIDBackplaneNetIronCes2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 1))
brcdEntityOIDBackplaneNetIronCer2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 2))
brcdEntityOIDBackplaneNetIronXMR = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 2, 3))
brcdEntityOIDBackplaneMlxFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3))
brcdEntityOIDBackplaneMLX = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3, 1))
brcdEntityOIDBackplaneMLXe = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 4, 3, 2))
brcdEntityOIDContainer = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5))
brcdEntityOIDContainerUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 1))
brcdEntityOIDContainerPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 2))
brcdEntityOIDContainerFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 3))
brcdEntityOIDContainerMgmtModuleSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 4))
brcdEntityOIDContainerSwitchFabricModuleSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 5))
brcdEntityOIDContainerIntfModuleSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 5, 6))
brcdEntityOIDPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6))
brcdEntityOIDPowerSupplyUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 1))
brcdEntityOIDPowerSupplyAC500W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 2))
brcdEntityOIDPowerSupplyDC500W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 3))
brcdEntityOIDPowerSupplyAC1200W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 4))
brcdEntityOIDPowerSupplyDC1200W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 5))
brcdEntityOIDPowerSupplyAC1200WA = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 6))
brcdEntityOIDPowerSupplyDC1200WA = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 7))
brcdEntityOIDPowerSupplyAC1800W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 8))
brcdEntityOIDPowerSupplyDC1800W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 9))
brcdEntityOIDPowerSupplyAC2100W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 10))
brcdEntityOIDPowerSupplyDC2100W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 11))
brcdEntityOIDPowerSupplyAC2400W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 12))
brcdEntityOIDPowerSupplyDC2400W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 13))
brcdEntityOIDPowerSupplyAC3000W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 14))
brcdEntityOIDPowerSupplyDC3000W = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 6, 15))
brcdEntityOIDFan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7))
brcdEntityOIDFanUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 1))
brcdEntityOIDChassisFanTray = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 2))
brcdEntityOIDChassisFan = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 7, 3))
brcdEntityOIDSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8))
brcdEntityOIDSensorUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 1))
brcdEntityOIDSensorChipTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 2))
brcdEntityOIDSensorModuleTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 8, 3))
brcdEntityOIDModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9))
brcdEntityOIDModuleUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 1))
brcdEntityOIDModuleMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2))
brcdEntityOIDModuleMgmtUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 1))
brcdEntityOIDModuleMgmtNetIronFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2))
brcdEntityOIDModuleMgmtNiMlxMr = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 1))
brcdEntityOIDModuleMgmtNiMlx32Mr = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 2))
brcdEntityOIDModuleMgmtNiXmrMr = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 3))
brcdEntityOIDModuleMgmtNiXmr32Mr = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 2, 4))
brcdEntityOIDModuleMgmtMlxFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3))
brcdEntityOIDModuleMgmtBrMlxMr2M = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 1))
brcdEntityOIDModuleMgmtBrMlxMr2X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 2))
brcdEntityOIDModuleMgmtBrMlx32Mr2M = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 3))
brcdEntityOIDModuleMgmtBrMlx32Mr2X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 2, 3, 4))
brcdEntityOIDModuleSfm = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3))
brcdEntityOIDModuleSfmUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 1))
brcdEntityOIDModuleSfmNetIronFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2))
brcdEntityOIDModuleSfmNiXSf1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 1))
brcdEntityOIDModuleSfmNiXSf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 2))
brcdEntityOIDModuleSfmNiX32Sf = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 3))
brcdEntityOIDModuleSfmNiX4Hsf = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 4))
brcdEntityOIDModuleSfmNiX16n8Hsf = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 5))
brcdEntityOIDModuleSfmNiX32Hsf = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 3, 2, 6))
brcdEntityOIDModuleIntf = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4))
brcdEntityOIDModuleIntfUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 1))
brcdEntityOIDModuleIntfNetIronFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2))
brcdEntityOIDModuleIntfNiMlx1Gx20Gc = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 1))
brcdEntityOIDModuleIntfNiXmr1Gx20Gc = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 2))
brcdEntityOIDModuleIntfNiMlx1Gx48Ta = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 3))
brcdEntityOIDModuleIntfNiMlx1Gx20Sfp = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 4))
brcdEntityOIDModuleIntfNiXmr1Gx20Sfp = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 5))
brcdEntityOIDModuleIntfNiMlx10Gx2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 6))
brcdEntityOIDModuleIntfNiXmr10Gx2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 7))
brcdEntityOIDModuleIntfNiMlx10Gx4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 8))
brcdEntityOIDModuleIntfNiXmr10Gx4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 9))
brcdEntityOIDModuleIntfNiMlx10Gx8D = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 10))
brcdEntityOIDModuleIntfNiMlx10Gx8M = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 2, 11))
brcdEntityOIDModuleIntfMlxFamily = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3))
brcdEntityOIDModuleIntfBrMlx1Gcx24X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 1))
brcdEntityOIDModuleIntfBrMlx1Gcx24xMl = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 2))
brcdEntityOIDModuleIntfBrMlx1Gfx24X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 3))
brcdEntityOIDModuleIntfBrMlx1Gfx24xMl = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 4))
brcdEntityOIDModuleIntfBrMlx10Gx4X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 5))
brcdEntityOIDModuleIntfBrMlx10Gx4xMl = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 6))
brcdEntityOIDModuleIntfBrMlx10Gx8X = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 7))
brcdEntityOIDModuleIntfBrMlx10Gx24Dm = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 8))
brcdEntityOIDModuleIntfBrMlx40Gx2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 9))
brcdEntityOIDModuleIntfBrMlx40Gx4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 10))
brcdEntityOIDModuleIntfBrMlx100Gx1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 11))
brcdEntityOIDModuleIntfBrMlx100Gx2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 12))
brcdEntityOIDModuleIntfBrMlx100Gx2CFP2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 13))
brcdEntityOIDModuleIntfBrMlx10Gx20 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 14))
brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 4, 3, 15))
brcdEntityOIDModuleOptics = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5))
brcdEntityOIDModuleOpticsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 1))
brcdEntityOIDModuleOpticsSFP = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 2))
brcdEntityOIDModuleOpticsSFPP = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 3))
brcdEntityOIDModuleOpticsXFP = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 4))
brcdEntityOIDModuleOpticsCFP = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 5))
brcdEntityOIDModuleOpticsQSFPP = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 6))
brcdEntityOIDModuleOpticsCFP2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 9, 5, 7))
brcdEntityOIDPort = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10))
brcdEntityOIDPortUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 1))
brcdEntityOIDPortMgmtSerial = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 2))
brcdEntityOIDPortMgmtEth = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 3))
brcdEntityOIDPort100BaseTx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 4))
brcdEntityOIDPort100BaseFx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 5))
brcdEntityOIDPortGigBaseTx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 6))
brcdEntityOIDPortGigBaseFx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 7))
brcdEntityOIDPort10GigBaseFx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 8))
brcdEntityOIDPort40GigBaseFx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 9))
brcdEntityOIDPort100GigBaseFx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 10))
brcdEntityOIDPort10GigBaseTx = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 10, 11))
brcdEntityOIDStack = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 11))
brcdEntityOIDStackUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 11, 1))
brcdEntityOIDCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12))
brcdEntityOIDCpuUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 1))
brcdEntityOIDCpuPPC7447A = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 2))
brcdEntityOIDCpuPPC7448 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 3))
brcdEntityOIDCpuPPC7451 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 4))
brcdEntityOIDCpuPPC7455 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 5))
brcdEntityOIDCpuPPC7457 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 6))
brcdEntityOIDCpuPPC8541 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 7))
brcdEntityOIDCpuPPC8541E = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 8))
brcdEntityOIDCpuPPC8544 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 9))
brcdEntityOIDCpuPPC8544E = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 10))
brcdEntityOIDCpuPPC8572 = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 11))
brcdEntityOIDCpuPPC8572E = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 17, 1, 12, 12))
mibBuilder.exportSymbols("BROCADE-ENTITY-OID-MIB", brcdEntityOIDChassisNetIronXMR16000=brcdEntityOIDChassisNetIronXMR16000, brcdEntityOIDModuleIntfNiMlx10Gx4=brcdEntityOIDModuleIntfNiMlx10Gx4, brcdEntityOIDModuleOpticsSFPP=brcdEntityOIDModuleOpticsSFPP, brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule=brcdEntityOIDModuleIntfBrMlx10Gx4IPSecModule, brcdEntityOIDChassisMLXe32=brcdEntityOIDChassisMLXe32, brcdEntityOIDBackplaneUnknown=brcdEntityOIDBackplaneUnknown, brcdEntityOIDModuleMgmtMlxFamily=brcdEntityOIDModuleMgmtMlxFamily, brcdEntityOIDPort100BaseTx=brcdEntityOIDPort100BaseTx, brcdEntityOIDModuleMgmtBrMlxMr2M=brcdEntityOIDModuleMgmtBrMlxMr2M, brcdEntityOIDPowerSupply=brcdEntityOIDPowerSupply, brcdEntityOIDPortGigBaseTx=brcdEntityOIDPortGigBaseTx, brcdEntityOIDCpuUnknown=brcdEntityOIDCpuUnknown, brcdEntityOIDCpuPPC8572E=brcdEntityOIDCpuPPC8572E, brcdEntityOIDContainerSwitchFabricModuleSlot=brcdEntityOIDContainerSwitchFabricModuleSlot, brcdEntityOIDCpu=brcdEntityOIDCpu, brcdEntityOIDChassisNetIronCes2048C=brcdEntityOIDChassisNetIronCes2048C, brcdEntityOIDChassisNetIronCer2024C4X=brcdEntityOIDChassisNetIronCer2024C4X, brcdEntityOIDPortGigBaseFx=brcdEntityOIDPortGigBaseFx, brcdEntityOIDModuleSfmNiX32Hsf=brcdEntityOIDModuleSfmNiX32Hsf, brcdEntityOIDModuleMgmtNetIronFamily=brcdEntityOIDModuleMgmtNetIronFamily, brcdEntityOIDModuleMgmtNiMlx32Mr=brcdEntityOIDModuleMgmtNiMlx32Mr, brcdEntityOIDModuleSfmNiXSf1=brcdEntityOIDModuleSfmNiXSf1, brcdEntityOIDModuleIntfBrMlx100Gx2=brcdEntityOIDModuleIntfBrMlx100Gx2, brcdEntityOIDPowerSupplyDC2100W=brcdEntityOIDPowerSupplyDC2100W, brcdEntityOIDCpuPPC8541=brcdEntityOIDCpuPPC8541, brcdEntityOIDPortMgmtSerial=brcdEntityOIDPortMgmtSerial, brcdEntityOIDModuleIntfNiXmr10Gx4=brcdEntityOIDModuleIntfNiXmr10Gx4, brcdEntityOIDModuleMgmt=brcdEntityOIDModuleMgmt, brcdEntityOIDCpuPPC7447A=brcdEntityOIDCpuPPC7447A, brcdEntityOIDChassisNetIronXMRFamily=brcdEntityOIDChassisNetIronXMRFamily, brcdEntityOIDContainerPowerSupply=brcdEntityOIDContainerPowerSupply, brcdEntityOIDModuleIntfBrMlx1Gcx24X=brcdEntityOIDModuleIntfBrMlx1Gcx24X, brcdEntityOIDContainerIntfModuleSlot=brcdEntityOIDContainerIntfModuleSlot, brcdEntityOIDModuleIntfNiXmr1Gx20Gc=brcdEntityOIDModuleIntfNiXmr1Gx20Gc, brcdEntityOIDModuleIntfNiXmr10Gx2=brcdEntityOIDModuleIntfNiXmr10Gx2, brcdEntityOIDContainerFanTray=brcdEntityOIDContainerFanTray, brcdEntityOIDBackplaneNetIronXMR=brcdEntityOIDBackplaneNetIronXMR, brcdEntityOIDBackplaneMLXe=brcdEntityOIDBackplaneMLXe, brcdEntityOIDModuleMgmtNiMlxMr=brcdEntityOIDModuleMgmtNiMlxMr, brcdEntityOIDChassisFanTray=brcdEntityOIDChassisFanTray, brcdEntityOIDPowerSupplyDC1800W=brcdEntityOIDPowerSupplyDC1800W, brcdEntityOIDUnknown=brcdEntityOIDUnknown, brcdEntityOIDPort=brcdEntityOIDPort, brcdEntityOIDModuleIntfNiMlx1Gx20Sfp=brcdEntityOIDModuleIntfNiMlx1Gx20Sfp, brcdEntityOIDChassisUnknown=brcdEntityOIDChassisUnknown, brcdEntityOIDModuleIntfNiMlx10Gx8M=brcdEntityOIDModuleIntfNiMlx10Gx8M, brcdEntityOIDModuleSfm=brcdEntityOIDModuleSfm, brcdEntityOIDChassisNetIronCes2024C4X=brcdEntityOIDChassisNetIronCes2024C4X, brcdEntityOIDModuleSfmNiXSf3=brcdEntityOIDModuleSfmNiXSf3, brcdEntityOIDCpuPPC8544E=brcdEntityOIDCpuPPC8544E, brcdEntityOIDModuleMgmtBrMlx32Mr2X=brcdEntityOIDModuleMgmtBrMlx32Mr2X, brcdEntityOIDModuleIntfBrMlx100Gx1=brcdEntityOIDModuleIntfBrMlx100Gx1, brcdEntityOIDCpuPPC8541E=brcdEntityOIDCpuPPC8541E, brcdEntityOIDModuleIntfNiMlx10Gx8D=brcdEntityOIDModuleIntfNiMlx10Gx8D, brcdEntityOIDModuleIntf=brcdEntityOIDModuleIntf, brcdEntityOIDModuleIntfBrMlx10Gx4X=brcdEntityOIDModuleIntfBrMlx10Gx4X, brcdEntityOIDModuleSfmNetIronFamily=brcdEntityOIDModuleSfmNetIronFamily, brcdEntityOIDCpuPPC8544=brcdEntityOIDCpuPPC8544, brcdEntityOIDModuleOpticsXFP=brcdEntityOIDModuleOpticsXFP, brcdEntityOIDModuleIntfBrMlx1Gcx24xMl=brcdEntityOIDModuleIntfBrMlx1Gcx24xMl, brcdEntityOIDChassisNetIronCes2048FX=brcdEntityOIDChassisNetIronCes2048FX, brcdEntityOIDPowerSupplyAC1200W=brcdEntityOIDPowerSupplyAC1200W, brcdEntityOIDModuleIntfBrMlx40Gx4=brcdEntityOIDModuleIntfBrMlx40Gx4, brcdEntityOIDModuleIntfBrMlx100Gx2CFP2=brcdEntityOIDModuleIntfBrMlx100Gx2CFP2, brcdEntityOIDChassisMLX32=brcdEntityOIDChassisMLX32, brcdEntityOIDChassisFan=brcdEntityOIDChassisFan, brcdEntityOIDSensorUnknown=brcdEntityOIDSensorUnknown, brcdEntityOIDPowerSupplyDC3000W=brcdEntityOIDPowerSupplyDC3000W, brcdEntityOIDModuleIntfBrMlx1Gfx24xMl=brcdEntityOIDModuleIntfBrMlx1Gfx24xMl, brcdEntityOIDPortUnknown=brcdEntityOIDPortUnknown, brcdEntityOIDChassisNetIronCer2048FX=brcdEntityOIDChassisNetIronCer2048FX, brcdEntityOIDModuleIntfBrMlx1Gfx24X=brcdEntityOIDModuleIntfBrMlx1Gfx24X, brcdEntityOIDModuleOpticsCFP2=brcdEntityOIDModuleOpticsCFP2, brcdEntityOIDModuleSfmNiX16n8Hsf=brcdEntityOIDModuleSfmNiX16n8Hsf, brcdEntityOIDStack=brcdEntityOIDStack, brcdEntityOIDModule=brcdEntityOIDModule, brcdEntityOIDCpuPPC7448=brcdEntityOIDCpuPPC7448, brcdEntityOIDSensorChipTemp=brcdEntityOIDSensorChipTemp, brcdEntityOIDStackUnknown=brcdEntityOIDStackUnknown, brcdEntityOIDPowerSupplyDC2400W=brcdEntityOIDPowerSupplyDC2400W, brcdEntityOIDModuleSfmNiX4Hsf=brcdEntityOIDModuleSfmNiX4Hsf, brcdEntityOIDModuleMgmtBrMlx32Mr2M=brcdEntityOIDModuleMgmtBrMlx32Mr2M, brcdEntityOIDChassisNetIronCes2024F4X=brcdEntityOIDChassisNetIronCes2024F4X, brcdEntityOIDModuleSfmNiX32Sf=brcdEntityOIDModuleSfmNiX32Sf, brcdEntityOIDModuleIntfNiMlx10Gx2=brcdEntityOIDModuleIntfNiMlx10Gx2, brcdEntityOIDModuleIntfBrMlx10Gx4xMl=brcdEntityOIDModuleIntfBrMlx10Gx4xMl, brcdEntityOIDCpuPPC7451=brcdEntityOIDCpuPPC7451, brcdEntityOIDFanUnknown=brcdEntityOIDFanUnknown, brcdEntityOIDChassisNetIronCer2024C=brcdEntityOIDChassisNetIronCer2024C, brcdEntityOIDModuleMgmtBrMlxMr2X=brcdEntityOIDModuleMgmtBrMlxMr2X, brcdEntityOIDMIB=brcdEntityOIDMIB, brcdEntityOIDContainerMgmtModuleSlot=brcdEntityOIDContainerMgmtModuleSlot, brcdEntityOIDBackplaneNetIronFamily=brcdEntityOIDBackplaneNetIronFamily, brcdEntityOIDChassisMLXFamily=brcdEntityOIDChassisMLXFamily, brcdEntityOIDPort100GigBaseFx=brcdEntityOIDPort100GigBaseFx, brcdEntityOIDChassisMLXeFamily=brcdEntityOIDChassisMLXeFamily, brcdEntityOIDChassis=brcdEntityOIDChassis, brcdEntityOIDBackplaneMLX=brcdEntityOIDBackplaneMLX, brcdEntityOIDBackplaneMlxFamily=brcdEntityOIDBackplaneMlxFamily, brcdEntityOIDChassisNetIronXMR4000=brcdEntityOIDChassisNetIronXMR4000, brcdEntityOIDChassisNetIronCer2048C=brcdEntityOIDChassisNetIronCer2048C, brcdEntityOIDBackplane=brcdEntityOIDBackplane, brcdEntityOIDBackplaneNetIronCer2000=brcdEntityOIDBackplaneNetIronCer2000, brcdEntityOIDModuleOptics=brcdEntityOIDModuleOptics, brcdEntityOIDModuleIntfBrMlx10Gx24Dm=brcdEntityOIDModuleIntfBrMlx10Gx24Dm, brcdEntityOIDPowerSupplyUnknown=brcdEntityOIDPowerSupplyUnknown, brcdEntityOIDModuleMgmtUnknown=brcdEntityOIDModuleMgmtUnknown, brcdEntityOIDChassisMLXe8=brcdEntityOIDChassisMLXe8, brcdEntityOIDPortMgmtEth=brcdEntityOIDPortMgmtEth, brcdEntityOIDPort10GigBaseFx=brcdEntityOIDPort10GigBaseFx, brcdEntityOIDPort10GigBaseTx=brcdEntityOIDPort10GigBaseTx, brcdEntityOIDModuleIntfNiMlx1Gx48Ta=brcdEntityOIDModuleIntfNiMlx1Gx48Ta, brcdEntityOIDChassisMLX4=brcdEntityOIDChassisMLX4, brcdEntityOIDPowerSupplyAC1800W=brcdEntityOIDPowerSupplyAC1800W, brcdEntityOIDChassisNetIronCer2000Family=brcdEntityOIDChassisNetIronCer2000Family, brcdEntityOIDModuleOpticsCFP=brcdEntityOIDModuleOpticsCFP, brcdEntityOIDSensor=brcdEntityOIDSensor, brcdEntityOIDPowerSupplyAC2400W=brcdEntityOIDPowerSupplyAC2400W, PYSNMP_MODULE_ID=brcdEntityOIDMIB, brcdEntityOIDChassisNetIronCes2048F=brcdEntityOIDChassisNetIronCes2048F, brcdEntityOIDChassisNetIronCer2048CX=brcdEntityOIDChassisNetIronCer2048CX, brcdEntityOIDModuleMgmtNiXmrMr=brcdEntityOIDModuleMgmtNiXmrMr, brcdEntityOIDModuleOpticsQSFPP=brcdEntityOIDModuleOpticsQSFPP, brcdEntityOIDBackplaneNetIronCes2000=brcdEntityOIDBackplaneNetIronCes2000, brcdEntityOIDChassisNetIronCer2024F=brcdEntityOIDChassisNetIronCer2024F, brcdEntityOIDModuleIntfNiXmr1Gx20Sfp=brcdEntityOIDModuleIntfNiXmr1Gx20Sfp, brcdEntityOIDOther=brcdEntityOIDOther, brcdEntityOIDSensorModuleTemp=brcdEntityOIDSensorModuleTemp, brcdEntityOIDChassisMLX8=brcdEntityOIDChassisMLX8, brcdEntityOIDContainerUnknown=brcdEntityOIDContainerUnknown, brcdEntityOIDModuleIntfBrMlx10Gx8X=brcdEntityOIDModuleIntfBrMlx10Gx8X, brcdEntityOIDCpuPPC7457=brcdEntityOIDCpuPPC7457, brcdEntityOIDModuleOpticsSFP=brcdEntityOIDModuleOpticsSFP, brcdEntityOIDModuleIntfBrMlx10Gx20=brcdEntityOIDModuleIntfBrMlx10Gx20, brcdEntityOIDMIBObjects=brcdEntityOIDMIBObjects, brcdEntityOIDChassisNetIronCes2000Family=brcdEntityOIDChassisNetIronCes2000Family, brcdEntityOIDModuleIntfBrMlx40Gx2=brcdEntityOIDModuleIntfBrMlx40Gx2, brcdEntityOIDChassisNetIronCes2048CX=brcdEntityOIDChassisNetIronCes2048CX, brcdEntityOIDPowerSupplyDC1200WA=brcdEntityOIDPowerSupplyDC1200WA, brcdEntityOIDModuleUnknown=brcdEntityOIDModuleUnknown, brcdEntityOIDModuleOpticsUnknown=brcdEntityOIDModuleOpticsUnknown, brcdEntityOIDChassisMLX16=brcdEntityOIDChassisMLX16, brcdEntityOIDContainer=brcdEntityOIDContainer, brcdEntityOIDModuleIntfMlxFamily=brcdEntityOIDModuleIntfMlxFamily, brcdEntityOIDPowerSupplyAC500W=brcdEntityOIDPowerSupplyAC500W, brcdEntityOIDPowerSupplyDC1200W=brcdEntityOIDPowerSupplyDC1200W, brcdEntityOIDCpuPPC7455=brcdEntityOIDCpuPPC7455, brcdEntityOIDModuleSfmUnknown=brcdEntityOIDModuleSfmUnknown, brcdEntityOIDModuleIntfNetIronFamily=brcdEntityOIDModuleIntfNetIronFamily, brcdEntityOIDPowerSupplyAC2100W=brcdEntityOIDPowerSupplyAC2100W, brcdEntityOIDChassisNetIronXMR32000=brcdEntityOIDChassisNetIronXMR32000, brcdEntityOIDPort100BaseFx=brcdEntityOIDPort100BaseFx, brcdEntityOIDPowerSupplyAC3000W=brcdEntityOIDPowerSupplyAC3000W, brcdEntityOIDChassisNetIronCer2024F4X=brcdEntityOIDChassisNetIronCer2024F4X, brcdEntityOIDPort40GigBaseFx=brcdEntityOIDPort40GigBaseFx, brcdEntityOIDChassisMLXe16=brcdEntityOIDChassisMLXe16, brcdEntityOIDPowerSupplyDC500W=brcdEntityOIDPowerSupplyDC500W, brcdEntityOIDCpuPPC8572=brcdEntityOIDCpuPPC8572, brcdEntityOIDFan=brcdEntityOIDFan, brcdEntityOIDPowerSupplyAC1200WA=brcdEntityOIDPowerSupplyAC1200WA, brcdEntityOIDChassisNetIronCes2024C=brcdEntityOIDChassisNetIronCes2024C, brcdEntityOIDModuleMgmtNiXmr32Mr=brcdEntityOIDModuleMgmtNiXmr32Mr, brcdEntityOIDModuleIntfUnknown=brcdEntityOIDModuleIntfUnknown, brcdEntityOIDModuleIntfNiMlx1Gx20Gc=brcdEntityOIDModuleIntfNiMlx1Gx20Gc, brcdEntityOIDChassisNetIronXMR8000=brcdEntityOIDChassisNetIronXMR8000, brcdEntityOIDChassisMLXe4=brcdEntityOIDChassisMLXe4, brcdEntityOIDChassisNetIronCes2024F=brcdEntityOIDChassisNetIronCes2024F, brcdEntityOIDChassisNetIronCer2048F=brcdEntityOIDChassisNetIronCer2048F)
