#
# PySNMP MIB module REDSTONE-IP-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-IP-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter32, TimeTicks, Unsigned32, MibIdentifier, Bits, IpAddress, ModuleIdentity, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "TimeTicks", "Unsigned32", "MibIdentifier", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rsIpPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 13))
rsIpPolicyMIB.setRevisions(('1998-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsIpPolicyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rsIpPolicyMIB.setLastUpdated('9801010000Z')
if mibBuilder.loadTexts: rsIpPolicyMIB.setOrganization('Redstone Communications, Inc.')
if mibBuilder.loadTexts: rsIpPolicyMIB.setContactInfo(' Redstone Communications, Inc. 5 Carlisle Road Westford MA 01886 USA Tel: +1-978-692-1999 Email: mib@redstonecom.com ')
if mibBuilder.loadTexts: rsIpPolicyMIB.setDescription('The IP Policy MIB for the Redstone Communications Inc. enterprise.')
rsIpPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1))
rsIpAccessList = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1))
rsIpAccessListTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: rsIpAccessListTable.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListTable.setDescription("This table contains entries for elements of IP access lists. Entries belonging to the same access list are ordered, and comparisons to those entries are performed in that order until a match is detected. If no match is found, the default action is to 'deny'.")
rsIpAccessListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListId"), (0, "REDSTONE-IP-POLICY-MIB", "rsIpAccessListElemId"))
if mibBuilder.loadTexts: rsIpAccessListEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListEntry.setDescription('Each entry describes the characteristics of an IP access list element.')
rsIpAccessListId = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 199)))
if mibBuilder.loadTexts: rsIpAccessListId.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListId.setDescription('The number of the access list to which this entry belongs.')
rsIpAccessListElemId = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)))
if mibBuilder.loadTexts: rsIpAccessListElemId.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListElemId.setDescription('The relative position of this entry within its access list. Access list entries are searched in this sequence (low to high values) until a match is found. NOTE: The value zero is reserved for use with SET operations to perform special-purpose table entry creations/deletions; see the DESCRIPTION of rsIpAccessListRowStatus for details. Get/GetNext/GetBulk retrievals never return an entry for which this object is zero-valued.')
rsIpAccessListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListRowStatus.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListRowStatus.setDescription('Controls creation/deletion of entries in this table according to the RowStatus textual convention, constrained to support the following values only: createAndGo destroy Two configuration levels are defined, limited and full. EARLY IMPLEMENTATIONS MIGHT PROVIDE ONLY THE LIMITED LEVEL OF CONFIGURATION CAPABILITY. *** LIMITED ACCESS LIST CONFIGURATION LEVEL *** 1) RowStatus createAndGo/destroy operations directed to a target table entry for which rsIpAccessListElemId is ZERO, have the following special-purpose semantics: createAndGo Create an entry having the specified configuration and append it to the target list, i.e. assign it a value of rsIpAccessListElemId that is one greater than the current last element in the list. destroy Destroy the specified list and all of its constituent elements. 2) RowStatus createAndGo/destroy operations directed to a target table entry for which rsIpAccessListElemId is NONZERO are disallowed. *** FULL ACCESS LIST CONFIGURATION LEVEL *** Permit conventional RowStatus-based management of table entries having a nonzero value for rsIpAccessListElemId, IN ADDITION TO the special RowStatus semantics applied to entries having a zero value for rsIpAccessListElemId. To create an entry in this table, the following entry objects MUST be explicitly configured: rsIpAccessListRowStatus In addition, when creating an entry the following conditions must hold: The value of rsIpAccessListElemId is nonzero. Once created, element attributes cannot be modified except by a RowStatus destroy operation to delete the list element.')
rsIpAccessListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("permit", 0), ("deny", 1))).clone('permit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListAction.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListAction.setDescription('Specifies the disposition of an item that matches the comparison criteria described by this entry.')
rsIpAccessListSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 5), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListSrc.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListSrc.setDescription('A source IP address. A subject IP address is first masked with the value of rsIpAccessListSrcMask, then the result is compared to this value. Setting both this object and its corresponding mask to 0.0.0.0 acts as a wildcard, matching any source IP address.')
rsIpAccessListSrcMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 6), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListSrcMask.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListSrcMask.setDescription('The IP address mask to be applied to a subject source IP address before comparing it to rsIpAccessListSrc. Ones in the mask identify which bits in the subject IP address are significant for the comparison. To be considered valid, a nonzero value for this object must contain a single contiguous string of ones, beginning with the most significant bit of the mask.')
rsIpAccessListDst = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 7), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListDst.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListDst.setDescription('A destination IP address. A subject IP address is first masked with the value of rsIpAccessListDstMask, then the result is compared to this value. Setting both this object and its corresponding mask to 0.0.0.0 acts as a wildcard, matching any destination IP address.')
rsIpAccessListDstMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 8), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListDstMask.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListDstMask.setDescription('The IP address mask to be applied to a subject destination IP address before comparing it to rsIpAccessListDst. Ones in the mask identify which bits in the IP address are significant for the comparison. To be considered valid, a nonzero value for this object must contain a single contiguous string of ones, beginning with the most significant bit of the mask.')
rsIpAccessListProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 13, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsIpAccessListProtocol.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListProtocol.setDescription('An IP Protocol value. Nonzero values match a specific IP Protocol value (e.g. 6 for TCP) carried in an IP packet; a value of zero acts as a wildcard, matching any IP Protocol.')
rsIpPolicyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4))
rsIpPolicyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1))
rsIpPolicyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2))
rsIpPolicyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 1, 1)).setObjects(("REDSTONE-IP-POLICY-MIB", "rsIpAccessListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpPolicyCompliance = rsIpPolicyCompliance.setStatus('current')
if mibBuilder.loadTexts: rsIpPolicyCompliance.setDescription('The compliance statement for entities which implement the Redstone IP Policy MIB.')
rsIpAccessListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 13, 4, 2, 1)).setObjects(("REDSTONE-IP-POLICY-MIB", "rsIpAccessListRowStatus"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListAction"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrc"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListSrcMask"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDst"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListDstMask"), ("REDSTONE-IP-POLICY-MIB", "rsIpAccessListProtocol"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsIpAccessListGroup = rsIpAccessListGroup.setStatus('current')
if mibBuilder.loadTexts: rsIpAccessListGroup.setDescription('A collection of objects for managing IP access list capabilities in a Redstone product.')
mibBuilder.exportSymbols("REDSTONE-IP-POLICY-MIB", rsIpAccessListId=rsIpAccessListId, rsIpAccessListRowStatus=rsIpAccessListRowStatus, rsIpAccessListSrc=rsIpAccessListSrc, PYSNMP_MODULE_ID=rsIpPolicyMIB, rsIpAccessListGroup=rsIpAccessListGroup, rsIpPolicyCompliance=rsIpPolicyCompliance, rsIpPolicyGroups=rsIpPolicyGroups, rsIpAccessListAction=rsIpAccessListAction, rsIpAccessListSrcMask=rsIpAccessListSrcMask, rsIpAccessListDstMask=rsIpAccessListDstMask, rsIpPolicyMIB=rsIpPolicyMIB, rsIpAccessListTable=rsIpAccessListTable, rsIpAccessListElemId=rsIpAccessListElemId, rsIpAccessListProtocol=rsIpAccessListProtocol, rsIpAccessList=rsIpAccessList, rsIpPolicyConformance=rsIpPolicyConformance, rsIpAccessListDst=rsIpAccessListDst, rsIpAccessListEntry=rsIpAccessListEntry, rsIpPolicyObjects=rsIpPolicyObjects, rsIpPolicyCompliances=rsIpPolicyCompliances)
