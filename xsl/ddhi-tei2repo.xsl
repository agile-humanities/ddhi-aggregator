<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xd tei"
    version="1.0">
    
    <xsl:output indent="yes"/>
    
    <xd:doc scope="stylesheet">
        <xd:desc>
            <xd:p><xd:b>Created on:</xd:b> Jan 8, 2021</xd:p>
            <xd:p><xd:b>Author:</xd:b> cwulfman</xd:p>
            <xd:p></xd:p>
        </xd:desc>
    </xd:doc>
    
    <xsl:template match="/">
        <interview>
            <identifier>
                <xsl:value-of select="//tei:idno[@type='DDHI']"/>
            </identifier>
            <title>
                <xsl:value-of select="//tei:teiHeader/tei:fileDesc/tei:titleStmt"/>
            </title>
            <primary_audio_URI>
                <xsl:apply-templates select="//tei:recording[@xml:id='primary_recording']" />
            </primary_audio_URI>
            <interview_body>
                <xsl:apply-templates select="tei:TEI/tei:text/tei:body" />
            </interview_body>
            <participants>
                <xsl:apply-templates select="tei:TEI/tei:teiHeader/tei:profileDesc/tei:particDesc" />
            </participants>
        </interview>
        <named_persons>
            <xsl:apply-templates select="tei:TEI/tei:standOff/tei:listPerson" />
        </named_persons>
        <named_places>
            <xsl:apply-templates select="tei:TEI/tei:standOff/tei:listPlace" />
        </named_places>
        <named_events>
            <xsl:apply-templates select="tei:TEI/tei:standOff/tei:listEvent" />
        </named_events>
        <named_orgs>
            <xsl:apply-templates select="tei:TEI/tei:standOff/tei:listOrg" />
        </named_orgs>
    </xsl:template>
    
    <xsl:template match="tei:body">
        <xsl:text>foo</xsl:text>
    </xsl:template>
    
    <xsl:template match="tei:particDesc">
        <xsl:apply-templates select="tei:person" />        
    </xsl:template>
    
    <xsl:template match="tei:person[ancestor::tei:particDesc]">
        <participant>
            <name><xsl:value-of select="tei:persName"/></name>
            <role><xsl:value-of select="@role"/></role>
        </participant>
    </xsl:template>
    
    <xsl:template match="tei:person[ancestor::tei:standOff]">
        <name><xsl:value-of select="tei:persName"/></name>
        <id type="DDHI"><xsl:value-of select="tei:idno"/></id>
    </xsl:template>
    
    <xsl:template match="tei:place[ancestor::tei:standOff]">
        <place><xsl:value-of select="tei:placeName"/></place>
        <id type="DDHI"><xsl:value-of select="tei:idno"/></id>
    </xsl:template>
    
    <xsl:template match="tei:org[ancestor::tei:standOff]">
        <org><xsl:value-of select="tei:orgName"/></org>
        <id type="DDHI"><xsl:value-of select="tei:idno"/></id>
    </xsl:template>
    
    <xsl:template match="tei:event[ancestor::tei:standOff]">
        <event><xsl:value-of select="tei:desc"/></event>
        <id type="DDHI"><xsl:value-of select="tei:idno"/></id>
    </xsl:template>
    
</xsl:stylesheet>