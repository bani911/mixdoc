# -*- coding: utf-8 -*-
# Dokumen Perijinan dan BPKB

from odoo import models, fields, api
from datetime import timedelta, date, datetime

class dokumen_file(models.Model):
    _name = 'dokumen.file'

    # no_dokumen = fields.Char(string="No.Dokumen", readonly=True)
    contact_person = fields.Many2one('res.users', 'PIC', domain="[('active','=','t')]")
    company_id = fields.Many2one('res.company', 'Organisasi', default=lambda self: self.env.user.company_id, readonly=True)
    jenis_dokumen = fields.Many2one('jenis.dokumen', 'Jenis Dokumen')
    # nama = fields.Char(string="Nama Dokumen", required=True)
    no_eksternal = fields.Char(string="No.Fisik Dokumen", required=True)
    perihal = fields.Char(string="Perihal", required=True)
    tgl_terbit = fields.Date('Tgl.Terbit/Tgl.Akta')
    tgl_expired = fields.Date('Tgl.Expired')
    tgl_perpanjangan = fields.Date('Tgl.Perpanjangan')
    # is_valid = fields.Boolean('is Valid?')
    keterangan = fields.Text('Keterangan')
    # kuasa_fisik = fields.Many2one('kuasa.fisik', 'Penguasaan Fisik')
    # luas = fields.Integer(string="Luas (M2)")
    # atas_nama = fields.Char(string="Atas Nama")
    # nilai_perolehan = fields.Float('Nilai Perolehan (Rp.)')
    notaris = fields.Char(string="Notaris")
    tempat_simpan = fields.Many2one('tempat.simpan', 'Penyimpanan')
    ket_simpan = fields.Char("Keterangan Simpan")
    jenis_unit = fields.Many2one('jenis.unit', 'Tipe Organisasi')
    bagian = fields.Many2one('bagian', 'Bagian', domain="[('tipe_org', '=', jenis_unit)]")
    penerbit = fields.Char("Penerbit")
    nama_dok = fields.Many2one('nama.dokumen', 'Nama Dokumen', domain="[('jenis_dokumen', '=', jenis_dokumen)]", required=True)
    item_list = fields.One2many('dokumen.item', 'list_id', 'Item List')

    _sql_constraints = [('cek_unik_nomor', 'UNIQUE(no_eksternal)', 'No.Fisik Dokumen tidak boleh sama!')]

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, rec.no_eksternal))
        return res

class dokumen_item(models.Model):
    _name = 'dokumen.item'

    list_id = fields.Many2one('dokumen.file', 'Reference')
    tgl_dok = fields.Date('Tgl.Dok', required=True)
    nama_dok = fields.Char('Nama Dokumen', required=True)
    tgl_terbit = fields.Date('Tgl.Terbit', required=True)
    lampiran_dok = fields.Binary("Lampiran")
