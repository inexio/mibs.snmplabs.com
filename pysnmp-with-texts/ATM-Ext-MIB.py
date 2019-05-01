#
# PySNMP MIB module ATM-Ext-MIB (http://pysnmp.sf.net)
# Produced by pysmi-0.0.1 from ATM-Ext-MIB at Fri May  8 19:35:23 2015
# On host cray platform Linux version 2.6.37.6-smp by user tt
# Using Python version 2.7.2 (default, Apr  2 2012, 20:32:47) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, enterprises, iso, Gauge32, MibIdentifier, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "enterprises", "iso", "Gauge32", "MibIdentifier", "Bits", "Counter32")
( DisplayString, RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus")
bellcore = MibIdentifier(enterprises.getName() + (148,))
requirements = MibIdentifier(bellcore.getName() + (1,))
atmExtMIB = MibIdentifier(requirements.getName() + (6,))
atmExtObjects = MibIdentifier(atmExtMIB.getName() + (1,))
atmExtContactTable = MibTable(atmExtObjects.getName() + (1,), )
if mibBuilder.loadTexts: atmExtContactTable.setDescription('A table with contact information for ATM\ninterfaces. ')
atmExtContactEntry = MibTableRow(atmExtContactTable.getName() + (1,), ).setIndexNames((0, "ATM-Ext-MIB", "ifIndex"))
if mibBuilder.loadTexts: atmExtContactEntry.setDescription('An entry in the Contact table.')
atmExtContactIfInfo = MibTableColumn(atmExtContactEntry.getName() + (2,), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmExtContactIfInfo.setDescription('The service provider contact information for\n                                  this interface.')
atmExtContactIfLocation = MibTableColumn(atmExtContactEntry.getName() + (3,), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmExtContactIfLocation.setDescription('The serving location of this interface.')
atmExtVclTable = MibTable(atmExtObjects.getName() + (2,), )
if mibBuilder.loadTexts: atmExtVclTable.setDescription('A table with performance information for VCLs. ')
atmExtVclEntry = MibTableRow(atmExtVclTable.getName() + (1,), ).setIndexNames((0, "ATM-Ext-MIB", "ifIndex"), (0, "ATM-Ext-MIB", "atmExtVclVpi"), (0, "ATM-Ext-MIB", "atmExtVclVci"))
if mibBuilder.loadTexts: atmExtVclEntry.setDescription('An entry in the VCL table.')
atmExtVclVpi = MibTableColumn(atmExtVclEntry.getName() + (1,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647)))
if mibBuilder.loadTexts: atmExtVclVpi.setDescription("The VCL's VPI value.")
atmExtVclVci = MibTableColumn(atmExtVclEntry.getName() + (2,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647)))
if mibBuilder.loadTexts: atmExtVclVci.setDescription("The VCL's VCI value.")
atmExtVclUpcViolations = MibTableColumn(atmExtVclEntry.getName() + (3,), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmExtVclUpcViolations.setDescription('The number of cells discarded due\n                                to UPC violations on this link.')
atmExtVclRowStatus = MibTableColumn(atmExtVclEntry.getName() + (4,), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmExtVclRowStatus.setDescription('The status of this entry.')
atmExtVplTable = MibTable(atmExtObjects.getName() + (3,), )
if mibBuilder.loadTexts: atmExtVplTable.setDescription('A table with performance information for\nVPLs. ')
atmExtVplEntry = MibTableRow(atmExtVplTable.getName() + (1,), ).setIndexNames((0, "ATM-Ext-MIB", "ifIndex"), (0, "ATM-Ext-MIB", "atmExtVplVpi"))
if mibBuilder.loadTexts: atmExtVplEntry.setDescription('An entry in the VPL table.')
atmExtVplVpi = MibTableColumn(atmExtVplEntry.getName() + (1,), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648,2147483647)))
if mibBuilder.loadTexts: atmExtVplVpi.setDescription("The VPL's VPI value.")
atmExtVplUpcViolations = MibTableColumn(atmExtVplEntry.getName() + (2,), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmExtVplUpcViolations.setDescription('The number of cells discarded due\n                                to UPC violations on this link.')
atmExtVplRowStatus = MibTableColumn(atmExtVplEntry.getName() + (3,), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmExtVplRowStatus.setDescription('The status of this entry.')
atmExtConformance = MibIdentifier(atmExtMIB.getName() + (2,))
atmExtGroups = MibIdentifier(atmExtConformance.getName() + (1,))
atmExtCompliances = MibIdentifier(atmExtConformance.getName() + (2,))
atmExtCompliance = MibIdentifier(atmExtCompliances.getName() + (1,))
atmExtContactGroup = MibIdentifier(atmExtGroups.getName() + (1,))
atmExtVCCGroup = MibIdentifier(atmExtGroups.getName() + (2,))
atmExtVPCGroup = MibIdentifier(atmExtGroups.getName() + (3,))
mibBuilder.exportSymbols("ATM-Ext-MIB", atmExtVplTable=atmExtVplTable, bellcore=bellcore, atmExtVclVpi=atmExtVclVpi, atmExtVplEntry=atmExtVplEntry, atmExtContactIfLocation=atmExtContactIfLocation, atmExtVplVpi=atmExtVplVpi, atmExtMIB=atmExtMIB, atmExtVclRowStatus=atmExtVclRowStatus, atmExtVclEntry=atmExtVclEntry, atmExtVCCGroup=atmExtVCCGroup, atmExtConformance=atmExtConformance, atmExtCompliances=atmExtCompliances, atmExtContactTable=atmExtContactTable, atmExtContactGroup=atmExtContactGroup, atmExtContactEntry=atmExtContactEntry, atmExtObjects=atmExtObjects, atmExtVplUpcViolations=atmExtVplUpcViolations, atmExtVclUpcViolations=atmExtVclUpcViolations, atmExtVclTable=atmExtVclTable, requirements=requirements, atmExtGroups=atmExtGroups, atmExtVplRowStatus=atmExtVplRowStatus, atmExtCompliance=atmExtCompliance, atmExtVclVci=atmExtVclVci, atmExtContactIfInfo=atmExtContactIfInfo, atmExtVPCGroup=atmExtVPCGroup)
