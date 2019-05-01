#
# PySNMP MIB module IANA-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-ENTITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:04:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
mib_2, Bits, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks, Counter32, Counter64, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "Bits", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaEntityMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 216))
ianaEntityMIB.setRevisions(('2015-07-16 00:00', '2015-07-16 00:00', '2013-04-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaEntityMIB.setRevisionsDescriptions(("Removed space between 'battery' and '(14)'.", 'Added storageDrive(15).', 'Initial version of this MIB as published in RFC 6933.',))
if mibBuilder.loadTexts: ianaEntityMIB.setLastUpdated('201507160000Z')
if mibBuilder.loadTexts: ianaEntityMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaEntityMIB.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 Phone: +1-310-301-5800 EMail: iana&iana.org')
if mibBuilder.loadTexts: ianaEntityMIB.setDescription("This MIB module defines a TEXTUAL-CONVENTION that provides an indication of the general hardware type of a particular physical entity. Copyright (c) 2013 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). The initial version of this MIB module was published in RFC 6933; for full legal notices see the RFC itself.")
class IANAPhysicalClass(TextualConvention, Integer32):
    description = "An enumerated value that provides an indication of the general hardware type of a particular physical entity. There are no restrictions as to the number of entPhysicalEntries of each entPhysicalClass, which must be instantiated by an agent. The enumeration 'other' is applicable if the physical entity class is known but does not match any of the supported values. The enumeration 'unknown' is applicable if the physical entity class is unknown to the agent. The enumeration 'chassis' is applicable if the physical entity class is an overall container for networking equipment. Any class of physical entity, except a stack, may be contained within a chassis; a chassis may only be contained within a stack. The enumeration 'backplane' is applicable if the physical entity class is some sort of device for aggregating and forwarding networking traffic, such as a shared backplane in a modular ethernet switch. Note that an agent may model a backplane as a single physical entity, which is actually implemented as multiple discrete physical components (within a chassis or stack). The enumeration 'container' is applicable if the physical entity class is capable of containing one or more removable physical entities, possibly of different types. For example, each (empty or full) slot in a chassis will be modeled as a container. Note that all removable physical entities should be modeled within a container entity, such as field-replaceable modules, fans, or power supplies. Note that all known containers should be modeled by the agent, including empty containers. The enumeration 'powerSupply' is applicable if the physical entity class is a power-supplying component. The enumeration 'fan' is applicable if the physical entity class is a fan or other heat-reduction component. The enumeration 'sensor' is applicable if the physical entity class is some sort of sensor, such as a temperature sensor within a router chassis. The enumeration 'module' is applicable if the physical entity class is some sort of self-contained sub-system. If the enumeration 'module' is removable, then it should be modeled within a container entity; otherwise, it should be modeled directly within another physical entity (e.g., a chassis or another module). The enumeration 'port' is applicable if the physical entity class is some sort of networking port, capable of receiving and/or transmitting networking traffic. The enumeration 'stack' is applicable if the physical entity class is some sort of super-container (possibly virtual) intended to group together multiple chassis entities. A stack may be realized by a 'virtual' cable, a real interconnect cable attached to multiple chassis, or multiple interconnect cables. A stack should not be modeled within any other physical entities, but a stack may be contained within another stack. Only chassis entities should be contained within a stack. The enumeration 'cpu' is applicable if the physical entity class is some sort of central processing unit. The enumeration 'energyObject' is applicable if the physical entity is some sort of energy object, i.e., a piece of equipment that is part of or attached to a communications network that is monitored, controlled, or aids in the management of another device for Energy Management. The enumeration 'battery' is applicable if the physical entity class is some sort of battery. The enumeration 'storageDrive' is applicable if the physical entity class is some sort of entity with data storage capability as main functionality, e.g. disk drive (HDD), solid state device (SSD), hybrid (SSHD), object storage (OSD) or other."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("chassis", 3), ("backplane", 4), ("container", 5), ("powerSupply", 6), ("fan", 7), ("sensor", 8), ("module", 9), ("port", 10), ("stack", 11), ("cpu", 12), ("energyObject", 13), ("battery", 14), ("storageDrive", 15))

mibBuilder.exportSymbols("IANA-ENTITY-MIB", IANAPhysicalClass=IANAPhysicalClass, PYSNMP_MODULE_ID=ianaEntityMIB, ianaEntityMIB=ianaEntityMIB)
